def whatsapp_webhook(request):
    """HTTP Cloud Function.
    Parameters
    ----------
    request (flask.Request) : The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>

    Returns
    -------
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.

    """
    country = request.values.get('Body', "").lower()
    resp = request.get(f'https://restcountries.eu/rest/v2/name/{country}?fullText=true')

    if not (200 <= resp.status_code <= 299):
        return 'Sorry we could not process your request. Please try again or check a different country'
    # Extract the single dict in the response using the index 0
    data = resp.json()[0]

    # Extract values needed by the bot
    native_name = data['nativeName']
    capital = data['capital']
    people = data['demonym']
    region = data['region']
    # Note the use of str.title() to improve readability of final response
    response = f"{country.title()} is a country in {region}. It's capital city is {capital}, while it's native name is {native_name}. A person from {country.title()} is called a {people}."

    return response
