from .configuration import ENDPOINT
from .configuration import MinosConfig
from .configuration import MinosConfigAbstract
from .configuration import REST
from minos.api_gateway.common.exceptions import EmptyMinosModelSequenceException
from minos.api_gateway.common.exceptions import MinosAttributeValidationException
from minos.api_gateway.common.exceptions import MinosConfigDefaultAlreadySetException
from minos.api_gateway.common.exceptions import MinosConfigException
from minos.api_gateway.common.exceptions import MinosException
from minos.api_gateway.common.exceptions import MinosImportException
from minos.api_gateway.common.exceptions import MinosMalformedAttributeException
from minos.api_gateway.common.exceptions import MinosMessageException
from minos.api_gateway.common.exceptions import MinosModelAttributeException
from minos.api_gateway.common.exceptions import MinosModelException
from minos.api_gateway.common.exceptions import MinosParseAttributeException
from minos.api_gateway.common.exceptions import MinosProtocolException
from minos.api_gateway.common.exceptions import (
    MinosRepositoryAggregateNotFoundException,
)
from minos.api_gateway.common.exceptions import MinosRepositoryDeletedAggregateException
from minos.api_gateway.common.exceptions import MinosRepositoryException
from minos.api_gateway.common.exceptions import (
    MinosRepositoryManuallySetAggregateIdException,
)
from minos.api_gateway.common.exceptions import (
    MinosRepositoryManuallySetAggregateVersionException,
)
from minos.api_gateway.common.exceptions import MinosRepositoryNonProvidedException
from minos.api_gateway.common.exceptions import MinosRepositoryUnknownActionException
from minos.api_gateway.common.exceptions import MinosReqAttributeException
from minos.api_gateway.common.exceptions import MinosTypeAttributeException
from minos.api_gateway.common.exceptions import MultiTypeMinosModelSequenceException

from .client import ClientHttp
