import attr
import enum


class TestDurationType(float):
    pass


class TestResultType(enum.Enum):
    Inconclusive = 'Inconclusive'
    Skipped = 'Skipped'
    Passed = 'Passed'
    Warning = 'Warning'
    Failed = 'Failed'


class FailureSiteType(enum.Enum):
    Test = 'Test'
    SetUp = 'SetUp'
    TearDown = 'TearDown'
    Parent = 'Parent'
    Child = 'Child'


class TestStatusType(enum.Enum):
    Inconclusive = 'Inconclusive'
    Skipped = 'Skipped'
    Passed = 'Passed'
    Warning = 'Warning'
    Failed = 'Failed'


class AssertionStatusType(enum.Enum):
    Inconclusive = 'Inconclusive'
    Passed = 'Passed'
    Warning = 'Warning'
    Failed = 'Failed'
    Error = 'Error'


class NonnegativeInt32(int):
    pass


class TestRunStateType(enum.Enum):
    NotRunnable = 'NotRunnable'
    Runnable = 'Runnable'
    Explicit = 'Explicit'
    Skipped = 'Skipped'
    Ignored = 'Ignored'


class TestSuiteTypeType(enum.Enum):
    GenericFixture = 'GenericFixture'
    ParameterizedFixture = 'ParameterizedFixture'
    Theory = 'Theory'
    GenericMethod = 'GenericMethod'
    ParameterizedMethod = 'ParameterizedMethod'
    Assembly = 'Assembly'
    SetUpFixture = 'SetUpFixture'
    TestFixture = 'TestFixture'
    TestMethod = 'TestMethod'
    TestSuite = 'TestSuite'


@attr.s
class TestRunType(object):
    command_line = attr.ib(metadata={"name": 'command-line', "type": 'element'}, type=str)
    filter = attr.ib(metadata={"name": 'filter', "type": 'element'}, type='TestFilterType')
    test_suite = attr.ib(
        metadata={"name": 'test-suite', "type": 'element'}, type='TestSuiteElementType'
    )
    test_case = attr.ib(
        metadata={"name": 'test-case', "type": 'element'}, type='TestCaseElementType'
    )
    test_suite = attr.ib(
        metadata={"name": 'test-suite', "type": 'element'},
        type='TestSuiteElementType',
        default=attr.NOTHING,
    )
    test_case = attr.ib(
        metadata={"name": 'test-case', "type": 'element'},
        type='TestCaseElementType',
        default=attr.NOTHING,
    )
    id_ = attr.ib(
        metadata={"name": 'id', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    name = attr.ib(
        metadata={"name": 'name', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    fullname = attr.ib(
        metadata={"name": 'fullname', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    testcasecount = attr.ib(
        metadata={"name": 'testcasecount', "type": 'attrib'},
        validator=attr.validators.instance_of(int),
    )
    result = attr.ib(
        metadata={"name": 'result', "type": 'attrib'}, validator=attr.validators.in_(TestResultType)
    )
    label = attr.ib(metadata={"name": 'label', "type": 'attrib'}, type=str, default=attr.NOTHING)
    start_time = attr.ib(
        metadata={"name": 'start-time', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    end_time = attr.ib(
        metadata={"name": 'end-time', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    duration = attr.ib(metadata={"name": 'duration', "type": 'attrib'}, default=attr.NOTHING)
    total = attr.ib(
        metadata={"name": 'total', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    passed = attr.ib(
        metadata={"name": 'passed', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    failed = attr.ib(
        metadata={"name": 'failed', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    inconclusive = attr.ib(
        metadata={"name": 'inconclusive', "type": 'attrib'},
        validator=attr.validators.instance_of(int),
    )
    skipped = attr.ib(
        metadata={"name": 'skipped', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    asserts = attr.ib(
        metadata={"name": 'asserts', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    random_seed = attr.ib(
        metadata={"name": 'random-seed', "type": 'attrib'},
        type=int,
        validator=attr.validators.instance_of(int),
    )


@attr.s
class TestFilterType(object):
    not_ = attr.ib(metadata={"name": 'not', "type": 'element'}, type='None', default=attr.NOTHING)
    and_ = attr.ib(
        metadata={"name": 'and', "type": 'element'}, type='CompositeFilterType', default=attr.NOTHING
    )
    or_ = attr.ib(
        metadata={"name": 'or', "type": 'element'}, type='CompositeFilterType', default=attr.NOTHING
    )
    cat = attr.ib(
        metadata={"name": 'cat', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    class_ = attr.ib(
        metadata={"name": 'class', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    test = attr.ib(
        metadata={"name": 'test', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    id_ = attr.ib(
        metadata={"name": 'id', "type": 'element'}, type='ValueMatchFilterType', default=attr.NOTHING
    )
    method = attr.ib(
        metadata={"name": 'method', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    namespace = attr.ib(
        metadata={"name": 'namespace', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    prop = attr.ib(metadata={"name": 'prop', "type": 'element'}, type='None', default=attr.NOTHING)
    name = attr.ib(
        metadata={"name": 'name', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )


@attr.s
class CompositeFilterType(object):
    not_ = attr.ib(metadata={"name": 'not', "type": 'element'}, type='None', default=attr.NOTHING)
    and_ = attr.ib(
        metadata={"name": 'and', "type": 'element'}, type='CompositeFilterType', default=attr.NOTHING
    )
    or_ = attr.ib(
        metadata={"name": 'or', "type": 'element'}, type='CompositeFilterType', default=attr.NOTHING
    )
    cat = attr.ib(
        metadata={"name": 'cat', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    class_ = attr.ib(
        metadata={"name": 'class', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    test = attr.ib(
        metadata={"name": 'test', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    id_ = attr.ib(
        metadata={"name": 'id', "type": 'element'}, type='ValueMatchFilterType', default=attr.NOTHING
    )
    method = attr.ib(
        metadata={"name": 'method', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    namespace = attr.ib(
        metadata={"name": 'namespace', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )
    prop = attr.ib(metadata={"name": 'prop', "type": 'element'}, type='None', default=attr.NOTHING)
    name = attr.ib(
        metadata={"name": 'name', "type": 'element'},
        type='ValueMatchFilterType',
        default=attr.NOTHING,
    )


@attr.s
class ValueMatchFilterType(object):
    re = attr.ib(metadata={"name": 're', "type": 'attrib'}, type=bool, default=attr.NOTHING)


@attr.s
class TestCaseElementType(object):
    properties = attr.ib(metadata={"name": 'properties', "type": 'element'}, type='PropertyBagType')
    environment = attr.ib(metadata={"name": 'environment', "type": 'element'}, type='None')
    settings = attr.ib(metadata={"name": 'settings', "type": 'element'}, type='None')
    failure = attr.ib(metadata={"name": 'failure', "type": 'element'}, type='None')
    reason = attr.ib(metadata={"name": 'reason', "type": 'element'}, type='None')
    output = attr.ib(metadata={"name": 'output', "type": 'element'}, type=str)
    assertions = attr.ib(metadata={"name": 'assertions', "type": 'element'}, type='None')
    id_ = attr.ib(
        metadata={"name": 'id', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    name = attr.ib(
        metadata={"name": 'name', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    fullname = attr.ib(
        metadata={"name": 'fullname', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    methodname = attr.ib(
        metadata={"name": 'methodname', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    classname = attr.ib(
        metadata={"name": 'classname', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    runstate = attr.ib(
        metadata={"name": 'runstate', "type": 'attrib'},
        validator=attr.validators.in_(TestRunStateType),
    )
    seed = attr.ib(
        metadata={"name": 'seed', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    result = attr.ib(
        metadata={"name": 'result', "type": 'attrib'}, validator=attr.validators.in_(TestStatusType)
    )
    label = attr.ib(metadata={"name": 'label', "type": 'attrib'}, type=str, default=attr.NOTHING)
    site = attr.ib(metadata={"name": 'site', "type": 'attrib'}, default=attr.NOTHING)
    start_time = attr.ib(
        metadata={"name": 'start-time', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    end_time = attr.ib(
        metadata={"name": 'end-time', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    duration = attr.ib(metadata={"name": 'duration', "type": 'attrib'}, default=attr.NOTHING)
    asserts = attr.ib(
        metadata={"name": 'asserts', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )


@attr.s
class TestSuiteElementType(object):
    properties = attr.ib(metadata={"name": 'properties', "type": 'element'}, type='PropertyBagType')
    test_suite = attr.ib(
        metadata={"name": 'test-suite', "type": 'element'}, type='TestSuiteElementType'
    )
    test_case = attr.ib(
        metadata={"name": 'test-case', "type": 'element'}, type='TestCaseElementType'
    )
    environment = attr.ib(metadata={"name": 'environment', "type": 'element'}, type='None')
    settings = attr.ib(metadata={"name": 'settings', "type": 'element'}, type='None')
    failure = attr.ib(metadata={"name": 'failure', "type": 'element'}, type='None')
    reason = attr.ib(metadata={"name": 'reason', "type": 'element'}, type='None')
    output = attr.ib(metadata={"name": 'output', "type": 'element'}, type=str)
    assertions = attr.ib(metadata={"name": 'assertions', "type": 'element'}, type='None')
    test_suite = attr.ib(
        metadata={"name": 'test-suite', "type": 'element'},
        type='TestSuiteElementType',
        default=attr.NOTHING,
    )
    test_case = attr.ib(
        metadata={"name": 'test-case', "type": 'element'},
        type='TestCaseElementType',
        default=attr.NOTHING,
    )
    id_ = attr.ib(
        metadata={"name": 'id', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    name = attr.ib(
        metadata={"name": 'name', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    fullname = attr.ib(
        metadata={"name": 'fullname', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    methodname = attr.ib(
        metadata={"name": 'methodname', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    classname = attr.ib(
        metadata={"name": 'classname', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    runstate = attr.ib(
        metadata={"name": 'runstate', "type": 'attrib'},
        validator=attr.validators.in_(TestRunStateType),
    )
    type_ = attr.ib(
        metadata={"name": 'type', "type": 'attrib'}, validator=attr.validators.in_(TestSuiteTypeType)
    )
    testcasecount = attr.ib(
        metadata={"name": 'testcasecount', "type": 'attrib'},
        validator=attr.validators.instance_of(int),
    )
    result = attr.ib(
        metadata={"name": 'result', "type": 'attrib'}, validator=attr.validators.in_(TestStatusType)
    )
    label = attr.ib(metadata={"name": 'label', "type": 'attrib'}, type=str, default=attr.NOTHING)
    site = attr.ib(metadata={"name": 'site', "type": 'attrib'}, default=attr.NOTHING)
    start_time = attr.ib(
        metadata={"name": 'start-time', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    end_time = attr.ib(
        metadata={"name": 'end-time', "type": 'attrib'}, type=str, default=attr.NOTHING
    )
    duration = attr.ib(metadata={"name": 'duration', "type": 'attrib'}, default=attr.NOTHING)
    asserts = attr.ib(
        metadata={"name": 'asserts', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    total = attr.ib(
        metadata={"name": 'total', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    passed = attr.ib(
        metadata={"name": 'passed', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    failed = attr.ib(
        metadata={"name": 'failed', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    warnings = attr.ib(
        metadata={"name": 'warnings', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )
    inconclusive = attr.ib(
        metadata={"name": 'inconclusive', "type": 'attrib'},
        validator=attr.validators.instance_of(int),
    )
    skipped = attr.ib(
        metadata={"name": 'skipped', "type": 'attrib'}, validator=attr.validators.instance_of(int)
    )


@attr.s
class PropertyBagType(object):
    property = attr.ib(metadata={"name": 'property', "type": 'element'}, type='PropertyType')


@attr.s
class PropertyType(object):
    name = attr.ib(
        metadata={"name": 'name', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )
    value = attr.ib(
        metadata={"name": 'value', "type": 'attrib'},
        type=str,
        validator=attr.validators.instance_of(str),
    )