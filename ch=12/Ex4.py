def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal server Error"
        
        case _:
            return "Unknown status"
        
print(https_status(5007))