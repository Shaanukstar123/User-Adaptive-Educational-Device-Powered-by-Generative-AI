from langchain_openai import AzureChatOpenAI  # Adjust based on actual import paths
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
import json
from dotenv import load_dotenv


# Import the necessary LangChain components

def initialiseAzureModel():
    load_dotenv()
    llm = AzureChatOpenAI(
        api_version=os.getenv("OPENAI_API_VERSION"),
        api_key=os.getenv("AZURE_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        azure_deployment="StoryGPT3"
    )
    output_parser = StrOutputParser()  # Converts output to string
    return llm, output_parser

def generateTitleWithLangChain(articles):
    load_dotenv()

    llm, output_parser = initialiseAzureModel()

    # Convert article list to a string format acceptable by our prompt
    dictToString = ""
    for article in articles:
        dictToString += str(article['id']) + ":" + article['name'] + ", "

    # Define the prompt template for topic choosing
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a topic chooser for a children's app. Given a list of article names and id, choose the articles that best represent trending topics around the world that kids would find interesting. Replace the names with a trending topic name and the other names replace with '_'. The name should represent what's trending around the world today relating to this news. Return in the same format and length. The topics should be very basic but also informative. E.g., Article about National Cinema Day = 'Cinema'. Return list of id: new name"),
        ("user", dictToString)
    ])

    # Main Chain
    chain = prompt | llm | output_parser
    output = chain.invoke({})
    return output

def getArticles(dir):
    with open(dir, 'r') as file:
        articles = json.load(file)
    return articles

def addNewNames(nameList, dir):
    if "\n" in nameList:
        nameList = nameList.split('\n')
    else:
        nameList = nameList.split(',')
    articleDict = {}
    for item in nameList:
        if ':' in item:
            id, new_name = item.split(':')
            articleDict[int(id)] = new_name.strip()

    with open(dir, 'r') as file:
        articles = json.load(file)
        for article in articles:
            if article['id'] in articleDict:
                article['new_title'] = articleDict[article['id']]

    with open(dir, 'w') as file:
        json.dump(articles, file, indent=2)

def generateNewNames():
    dir = 'data/output.json'
    articles = getArticles(dir)
    newNames = generateTitleWithLangChain(articles)
    addNewNames(newNames, dir)

#generateNewNames()
