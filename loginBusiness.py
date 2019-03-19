def validateUserSession(tokenSessionAfterGetRequest, tokenSessionAfterPostRequest):
    if tokenSessionAfterGetRequest == tokenSessionAfterPostRequest:
        return True
    else:
        return False