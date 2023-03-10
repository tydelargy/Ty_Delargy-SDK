#System Design

I chose to mirror the existing API functionality closely while adding some additional functionality.

_id is a parameter which can be used in all calls, and is present in all api responses to uniquely identify all items in a response. This makes further calls for developers easy to daisy chain, if they wish to use an ID to identify other return objects in th call.

The format for return is in a list of json objects, making it easy to index through returns and pull out key information. In practice, given the nested json return, I chose to remove the 'docs' tag since this was everpresent, and simply present users with a list of json objects for each return. In a single return scenario it is easy enough to index to 0 for the list, but since all returns have the option to return many json objects, a basic list made the most sense for utility.

For testing I decided to use Pytest as I am familiar with it and it is a quality package I am familiar with and fine readable and easy to use.