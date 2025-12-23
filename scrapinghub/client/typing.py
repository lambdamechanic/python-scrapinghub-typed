from __future__ import absolute_import

from typing import Any, Dict, Iterable, List, Literal, Tuple, TypedDict, Union

ProjectIdInput = Union[int, str]
JobKey = str
SpiderName = str
Tag = str
TagList = List[Tag]
TagInput = Union[Tag, TagList]
MetaField = str
MetaFields = Union[MetaField, List[MetaField]]
TimestampMs = int
AuthInput = Union[str, Tuple[str, str]]

JobState = Literal["pending", "running", "finished", "deleted"]


class ProjectSummary(TypedDict):
    project: int
    pending: int
    running: int
    finished: int
    has_capacity: bool


class JobSummary(TypedDict, total=False):
    close_reason: str
    elapsed: int
    finished_time: TimestampMs
    items: int
    key: JobKey
    logs: int
    pages: int
    pending_time: TimestampMs
    running_time: TimestampMs
    spider: SpiderName
    state: JobState
    ts: TimestampMs
    version: str


class JobSummaryGroup(TypedDict):
    count: int
    name: JobState
    summary: List[JobSummary]


class SpiderSummary(TypedDict):
    id: str
    tags: List[str]
    type: str
    version: str


class CollectionSummary(TypedDict):
    name: str
    type: str


class ActivityEvent(TypedDict, total=False):
    event: str
    job: JobKey
    user: str


class RequestItem(TypedDict, total=False):
    duration: int
    fp: str
    method: str
    rs: int
    status: int
    time: TimestampMs
    url: str


class LogEntry(TypedDict, total=False):
    level: int
    message: str
    time: TimestampMs


class FrontierQueueBatch(TypedDict, total=False):
    id: str
    requests: List[List[Any]]


FilterCondition = Union[str, List[Any]]
FilterParam = Union[str, List[FilterCondition]]
LogLevelName = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL", "SILENT"]

ParamsDict = Dict[str, Any]


class HubstorageClientOptions(TypedDict, total=False):
    endpoint: str
    connection_timeout: Union[int, float]
    max_retries: int
    max_retry_time: int
    user_agent: str
    use_msgpack: bool
