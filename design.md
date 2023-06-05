# Design

## Forcing API calls through `Client`

The idea was to "force" API calls to go through `lotr_sdk.client.Client` so that users
would be conscious that these calls are using network resources.
I considered making `Movie.get_quotes()` as it can also give the idea around the network call,
but for this one I decided to keep it simple.

## A single method for each endpoint

I've also decided for specific methods like `Client.get_movie()` and `Client.get_movies()` to
make it more intuitive. The alternative would be some sort of method overload with `Client.movie(optional_id)`
and then decide to return all movies or just a single one based on the optional ID.
Though, it would require some extra validates, like pagination, filtering and sorting as they don't seem
to be valid when getting a single resource.
So, my decision was mainly around these ideas.

## Filtering, Pagination, Sorting (fps)

I decided to use specific classes for each to avoid working directly with strings.
Though, there's still a limitation in this solution.
When referencing the fields, the user still needs to know the name in the API and not the actual field in the SDK.
I wanted to make it like `fps.Asc(Movie.name)` or `fps.Exists(Quote.dialog)`, but I was out of time.
Anyway, I decided to keep it this way as it seems better to support filtering/sorting even if
requiring to reference the API than not supporting it at all.

## HTTP client

By default, this SDK uses `requests` for HTTP calls.
Though, it is quite extensible.
I decided to make the HTTP client as extensible as possible so that users can customize it the way they need.
For example, if they need to set some sort of proxying, it is possible to extend the current implementation to do so.
Similarly, if they want to use some other library that is not `requests`, it is also possible.
Another thing I keptin mind for this HTTP client, was adding new functionality. Take as example the caching approach shown in `README.md`.
In the same way, if the user wants to change the behavior around `429` (say that they want to wait and retry), it is possible.
My intent was to provide caching and custom `429` retry with wait with the SDK, but due to time constraints, I left it out.
In any case, it is fairly simple to add it.

## Tests

I built this SDK using TDD, so all classes should covered with some tests.
I also included a `test_api` which is and end to end test to ensure things are working as expected.