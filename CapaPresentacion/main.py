import pprint

from agents import langchain_executor
from CapaDatos.models import Chat, Message, SenderEnum
from CapaNegocio.routeAgent import route_query

chat = Chat()
print(chat.status)
while True:
    user_query = input("User: ")
    chat.status = route_query(user_query)
    ai_response = langchain_executor.invoke(query=user_query, chat_history=chat)
    print(chat.status)
    human_message = Message(sender=SenderEnum.HumanMessage, message=user_query)
    ai_message = Message(sender=SenderEnum.AIMessage, message=ai_response)
    chat.messages.extend([human_message, ai_message])
    pprint.pprint(ai_response)

