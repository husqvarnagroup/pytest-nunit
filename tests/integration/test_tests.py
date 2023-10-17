"""
Test various scenarios
"""
import os

import xmlschema

import xml.dom.minidom


def test_passing_test(testdir, tmpdir):
    """
    Test a basic passing test
    """
    testdir.makepyfile(
        """
        def test_pass():
            assert 1 == 1
    """
    )
    outfile = tmpdir.join("out.xml")
    outfile_pth = str(outfile)

    result = testdir.runpytest("-v", "--nunit-xml=" + outfile_pth)
    result.stdout.fnmatch_lines(["*test_pass PASSED*"])
    assert result.ret == 0
    os.path.exists(outfile_pth)
    xs = xmlschema.XMLSchema(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "../../ext/nunit-src/TestResult.xsd",
        ),
        validation="lax",
    )
    out = xs.to_dict(outfile_pth)
    assert out["@total"] == 1
    assert out["@passed"] == 1
    assert out["@failed"] == 0
    assert out["test-suite"]["@total"] == 1
    assert out["test-suite"]["@passed"] == 1
    assert out["test-suite"]["@failed"] == 0
    assert out["test-suite"]["@skipped"] == 0


def test_failing_test(testdir, tmpdir):
    """
    Test a basic failing test
    """
    testdir.makepyfile(
        """
        def test_fail():
            assert 1 == 0
    """
    )
    outfile = tmpdir.join("out.xml")
    outfile_pth = str(outfile)

    result = testdir.runpytest("-v", "--nunit-xml=" + outfile_pth)
    result.stdout.fnmatch_lines(["*test_fail FAILED*"])
    assert result.ret != 0
    os.path.exists(outfile_pth)
    xs = xmlschema.XMLSchema(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "../../ext/nunit-src/TestResult.xsd",
        ),
        validation="lax",
    )
    out = xs.to_dict(outfile_pth)
    assert out["@total"] == 1, out
    assert out["@passed"] == 0, out
    assert out["@failed"] == 1, out
    assert out["@skipped"] == 0, out
    assert out["test-suite"]["@total"] == 1
    assert out["test-suite"]["@passed"] == 0
    assert out["test-suite"]["@failed"] == 1
    assert out["test-suite"]["@skipped"] == 0


def test_skipped_test(testdir, tmpdir):
    """
    Test a basic skipped test
    """
    testdir.makepyfile(
        """
        import pytest

        @pytest.mark.skip()
        def test_skip():
            assert 1 == 1
    """
    )
    outfile = tmpdir.join("out.xml")
    outfile_pth = str(outfile)

    result = testdir.runpytest("-v", "--nunit-xml=" + outfile_pth)
    result.stdout.fnmatch_lines(["*test_skip SKIPPED*"])
    assert result.ret == 0
    os.path.exists(outfile_pth)
    xs = xmlschema.XMLSchema(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "../../ext/nunit-src/TestResult.xsd",
        ),
        validation="lax",
    )
    out = xs.to_dict(outfile_pth)
    assert out["@total"] == 1, out
    assert out["@passed"] == 0, out
    assert out["@failed"] == 0, out
    assert out["@skipped"] == 1, out
    assert out["test-suite"]["@total"] == 1
    assert out["test-suite"]["@passed"] == 0
    assert out["test-suite"]["@failed"] == 0
    assert out["test-suite"]["@skipped"] == 1


def test_all_outcomes(testdir, tmpdir):
    """
    Test all 3 types of outcomes
    """
    testdir.makepyfile(
        """
        import pytest

        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 0

        @pytest.mark.skip()
        def test_skip():
            assert 1 == 1
    """
    )
    outfile = tmpdir.join("out.xml")
    outfile_pth = str(outfile)

    result = testdir.runpytest("-v", "--nunit-xml=" + outfile_pth)
    result.stdout.fnmatch_lines(["*test_pass PASSED*"])
    result.stdout.fnmatch_lines(["*test_fail FAILED*"])
    result.stdout.fnmatch_lines(["*test_skip SKIPPED*"])

    assert result.ret != 0
    os.path.exists(outfile_pth)
    xs = xmlschema.XMLSchema(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "../../ext/nunit-src/TestResult.xsd",
        ),
        validation="lax",
    )
    out = xs.to_dict(outfile_pth)
    assert out["@total"] == 3, out
    assert out["@passed"] == 1, out
    assert out["@failed"] == 1, out
    assert out["@skipped"] == 1, out


def test_error_test(testdir, tmpdir):
    """
    Test a test that fails
    """
    testdir.makepyfile(
        """
        def test_error(test_madeup_fixture):
            assert 1 == 1
    """
    )
    outfile = tmpdir.join("out.xml")
    outfile_pth = str(outfile)

    result = testdir.runpytest("-v", "--nunit-xml=" + outfile_pth)
    result.stdout.fnmatch_lines(["*test_error ERROR*"])
    assert result.ret != 0
    os.path.exists(outfile_pth)
    xs = xmlschema.XMLSchema(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "../../ext/nunit-src/TestResult.xsd",
        ),
        validation="lax",
    )
    out = xs.to_dict(outfile_pth)
    assert out["@total"] == 1, out
    assert out["@passed"] == 0, out
    assert out["@failed"] == 1, out
    assert out["@skipped"] == 0, out
    assert out["test-suite"]["@total"] == 1
    assert out["test-suite"]["@passed"] == 0
    assert out["test-suite"]["@failed"] == 1
    assert out["test-suite"]["@skipped"] == 0


def test_failing_fixture(testdir, tmpdir):
    """
    Test resolving issue # 55
    https://github.com/pytest-dev/pytest-nunit/issues/55
    """
    testdir.makepyfile(
        """
    import pytest
    
    @pytest.fixture(scope="class")
    def failing_fixture():
        raise Exception("SomeException")
    
    @pytest.mark.usefixtures("failing_fixture")
    class TestOne:
        def test_one(self):
            pass
    
        @pytest.mark.xfail(reason="No reason")
        def test_two(self):
            pytest.fail()
    """
    )
    outfile = tmpdir.join("out.xml")
    outfile_pth = str(outfile)

    result = testdir.runpytest("-v", "--nunit-xml=" + outfile_pth)
    assert int(result.ret) == 1
    assert "".join(result.stderr.lines) == ""
    result.stdout.fnmatch_lines(["*test_one ERROR*"])
    result.stdout.fnmatch_lines(["*test_two XFAIL*"])


def test_failing_fixture_flaky(testdir, tmpdir):
    testdir.makepyfile(
        """
    import pytest
    from flaky import flaky

    @pytest.fixture(scope="function")
    def failing_fixture():
        raise Exception("SomeException")

        yield

    @flaky(max_runs=3, min_passes=1)
    def test_one(failing_fixture):
        pass
    """
    )
    outfile = tmpdir.join("out.xml")
    outfile_pth = str(outfile)

    result = testdir.runpytest("--setup-plan")
    result = testdir.runpytest("-v", "--nunit-xml=" + outfile_pth)

    with open(outfile_pth) as f:
        s = f.read()
        temp = xml.dom.minidom.parseString(s)
        print(temp.toprettyxml())

    assert int(result.ret) == 1
    assert "".join(result.stderr.lines) == ""
    result.stdout.fnmatch_lines(["*test_one ERROR*"])
