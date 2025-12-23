# Documented Client API Inventory

Source of truth for documented API scope: docs/client/apidocs.rst (automodule with members + inherited members).

## Module: scrapinghub.client (__init__.py)
Classes and public methods:
- ScrapinghubClient
  - __init__(auth=None, dash_endpoint=None, connection_timeout=DEFAULT_CONNECTION_TIMEOUT, **kwargs)
  - get_project(project_id)
  - get_job(job_key)
  - close(timeout=None)
- Connection (internal helper, but exported via automodule)
  - _request(*args, **kwargs)
- HubstorageClient (internal helper, but exported via automodule)
  - request(*args, **kwargs)

Notes/constraints:
- auth supports API key or job auth (parse_auth); job key format is project/spider/job id.

## Module: scrapinghub.client.activity
Classes and public methods:
- Activity
  - iter(count=None, **params)
  - add(values, **kwargs)

Notes/constraints:
- add values: dicts with keys event/job/user; job must belong to same project.

## Module: scrapinghub.client.collections
Classes and public methods:
- Collections
  - get(type_, name)
  - get_store(name)
  - get_cached_store(name)
  - get_versioned_store(name)
  - get_versioned_cached_store(name)
  - iter()
  - list()
- Collection
  - get(key, **params)
  - set(value)
  - delete(keys)
  - truncate()
  - count(*args, **kwargs)
  - iter(key=None, prefix=None, prefixcount=None, startts=None, endts=None, requests_params=None, **params)
  - list(key=None, prefix=None, prefixcount=None, startts=None, endts=None, requests_params=None, **params)
  - create_writer(start=0, auth=None, size=1000, interval=15, qsize=None, content_encoding='identity', maxitemsize=1024 ** 2, callback=None)

Notes/constraints:
- collection types: 's' (store), 'cs' (cached store), 'vs' (versioned store), 'vcs' (versioned cached store).

## Module: scrapinghub.client.frontiers
Classes and public methods:
- Frontiers
  - get(name)
  - iter()
  - list()
  - newcount (property)
  - flush()
  - close()
- Frontier
  - get(slot)
  - iter()
  - list()
  - flush()
  - newcount (property)
- FrontierSlot
  - f (property)
  - q (property)
  - delete()
  - flush()
  - newcount (property)
- FrontierSlotFingerprints
  - add(fps)
  - iter(**params)
  - list(**params)
- FrontierSlotQueue
  - add(fps)
  - iter(mincount=None, **params)
  - list(mincount=None, **params)
  - delete(ids)

## Module: scrapinghub.client.items
Classes and public methods:
- Items (inherits _DownloadableProxyMixin, _ItemsResourceProxy)
  - list_iter(chunksize=1000, *args, **kwargs)
  - get(key, **params) [inherited]
  - write(item) [inherited]
  - iter(_key=None, count=None, **params) [inherited]
  - list(*args, **kwargs) [inherited]
  - flush() [inherited]
  - stats() [inherited]
  - close(block=True) [inherited]

Notes/constraints:
- iter filters use update_kwargs and _format_iter_filters (filter accepts list of strings or tuples/lists).

## Module: scrapinghub.client.logs
Classes and public methods:
- Logs (inherits _DownloadableProxyMixin, _ItemsResourceProxy)
  - log(message, level=logging.INFO, ts=None, **other)
  - debug(message, **other)
  - info(message, **other)
  - warn(message, **other) / warning alias
  - error(message, **other)
  - batch_write_start()
  - get(key, **params) [inherited]
  - write(item) [inherited]
  - iter(_key=None, count=None, **params) [inherited]
  - list(*args, **kwargs) [inherited]
  - flush() [inherited]
  - stats() [inherited]
  - close(block=True) [inherited]

Notes/constraints:
- log level values are defined in utils.LogLevel (DEBUG/INFO/WARNING/ERROR/CRITICAL/SILENT).

## Module: scrapinghub.client.requests
Classes and public methods:
- Requests (inherits _DownloadableProxyMixin, _ItemsResourceProxy)
  - add(url, status, method, rs, duration, ts, parent=None, fp=None)
  - get(key, **params) [inherited]
  - write(item) [inherited]
  - iter(_key=None, count=None, **params) [inherited]
  - list(*args, **kwargs) [inherited]
  - flush() [inherited]
  - stats() [inherited]
  - close(block=True) [inherited]

## Module: scrapinghub.client.samples
Classes and public methods:
- Samples (inherits _ItemsResourceProxy)
  - get(key, **params) [inherited]
  - write(item) [inherited]
  - iter(_key=None, count=None, **params) [inherited]
  - list(*args, **kwargs) [inherited]
  - flush() [inherited]
  - stats() [inherited]
  - close(block=True) [inherited]

## Module: scrapinghub.client.jobs
Classes and public methods:
- Jobs
  - count(spider=None, state=None, has_tag=None, lacks_tag=None, startts=None, endts=None, **params)
  - cancel(keys=None, count=None, **params)
  - iter(count=None, start=None, spider=None, state=None, has_tag=None, lacks_tag=None, startts=None, endts=None, meta=None, **params)
  - list(count=None, start=None, spider=None, state=None, has_tag=None, lacks_tag=None, startts=None, endts=None, meta=None, **params)
  - run(spider=None, units=None, priority=None, meta=None, add_tag=None, job_args=None, job_settings=None, cmd_args=None, environment=None, **params)
  - get(job_key)
  - summary(state=None, spider=None, **params)
  - iter_last(start=None, start_after=None, count=None, spider=None, **params)
  - update_tags(add=None, remove=None, spider=None)
- Job
  - update_tags(add=None, remove=None)
  - close_writers()
  - start(**params)
  - finish(**params)
  - delete(**params)
  - update(state, **params)
  - cancel()
- JobMeta (inherits _MappingProxy)
  - get(key) [inherited]
  - set(key, value) [inherited]
  - update(values) [inherited]
  - delete(key) [inherited]
  - iter() [inherited]
  - list(*args, **kwargs) [inherited]

Notes/constraints:
- Job states documented in docs/client/overview.rst: pending, running, finished, deleted.
- Job key format is project_id/spider_id/job_id (parse_job_key).

## Module: scrapinghub.client.projects
Classes and public methods:
- Projects
  - get(project_id)
  - list()
  - iter()
  - summary(state=None, **params)
- Project
  - no public methods; exposes sub-resources (jobs, spiders, activity, collections, frontiers, settings)
- Settings (inherits _MappingProxy)
  - get(key) [inherited]
  - set(key, value) [inherited]
  - update(values) [inherited]
  - delete(key) [inherited]
  - iter() [inherited]
  - list(*args, **kwargs) [inherited]

## Module: scrapinghub.client.spiders
Classes and public methods:
- Spiders
  - get(spider, **params)
  - list()
  - iter()
- Spider
  - update_tags(add=None, remove=None)
  - list_tags()

## Module: scrapinghub.client.exceptions
Classes and public methods:
- Exception classes only; no signature changes required.
