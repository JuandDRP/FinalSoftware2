from CapaDatos import models


def route_query(user_query):
    if "politica" in user_query.lower() or "cancelación" in user_query.lower():
        return (
            models.ChatStatus.status2
        )
    elif "precio" in user_query.lower() or "costo" in user_query.lower():
        return models.ChatStatus.status2  
    else:
        return models.ChatStatus.status1  
