{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNsJ8rxLR6+hy785TboiAYx",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/arka-siuu/CrackYourInternship/blob/main/gitagpt.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "KtM0SZLm-D0_"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "\n",
        "# Load the synthetic dataset\n",
        "data = {\n",
        "    'Keywords': [\"hello, hi, greetings\", \"product, info, details\", \"pricing, cost, charge\", \"support, help, assistance\", \"hours, operation, open\", \"location, office, address\"],\n",
        "    'Answers': [\n",
        "        \"Hello! How can I assist you today?\",\n",
        "        \"Our product is a next-gen AI tool for automation.\",\n",
        "        \"The pricing starts at $99 per month.\",\n",
        "        \"You can reach our support team at support@xyz.com.\",\n",
        "        \"We're open from 9 AM to 5 PM, Monday to Friday.\",\n",
        "        \"Our office is located in New York City.\"\n",
        "    ]\n",
        "}\n",
        "\n",
        "df = pd.DataFrame(data)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install fuzzywuzzy[speedup]\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EaBHa3c0-ICp",
        "outputId": "abf770a5-00a7-42b3-b542-4a3454ad9907"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting fuzzywuzzy[speedup]\n",
            "  Downloading fuzzywuzzy-0.18.0-py2.py3-none-any.whl.metadata (4.9 kB)\n",
            "Collecting python-levenshtein>=0.12 (from fuzzywuzzy[speedup])\n",
            "  Downloading python_Levenshtein-0.25.1-py3-none-any.whl.metadata (3.7 kB)\n",
            "Collecting Levenshtein==0.25.1 (from python-levenshtein>=0.12->fuzzywuzzy[speedup])\n",
            "  Downloading Levenshtein-0.25.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.3 kB)\n",
            "Collecting rapidfuzz<4.0.0,>=3.8.0 (from Levenshtein==0.25.1->python-levenshtein>=0.12->fuzzywuzzy[speedup])\n",
            "  Downloading rapidfuzz-3.9.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)\n",
            "Downloading python_Levenshtein-0.25.1-py3-none-any.whl (9.4 kB)\n",
            "Downloading Levenshtein-0.25.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (177 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m177.4/177.4 kB\u001b[0m \u001b[31m1.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading fuzzywuzzy-0.18.0-py2.py3-none-any.whl (18 kB)\n",
            "Downloading rapidfuzz-3.9.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.4 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.4/3.4 MB\u001b[0m \u001b[31m18.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: fuzzywuzzy, rapidfuzz, Levenshtein, python-levenshtein\n",
            "Successfully installed Levenshtein-0.25.1 fuzzywuzzy-0.18.0 python-levenshtein-0.25.1 rapidfuzz-3.9.6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from fuzzywuzzy import process\n",
        "\n",
        "def get_response(user_input):\n",
        "    best_match = None\n",
        "    best_score = 0\n",
        "    for index, row in df.iterrows():\n",
        "        keywords = row['Keywords'].split(', ')\n",
        "        for keyword in keywords:\n",
        "            match_score = process.extractOne(keyword, user_input.split())\n",
        "            if match_score[1] > best_score:\n",
        "                best_match = row['Answers']\n",
        "                best_score = match_score[1]\n",
        "    if best_score > 70:  # Adjust threshold as needed\n",
        "        return best_match\n",
        "    else:\n",
        "        return \"Sorry, I didn't understand that.\"\n"
      ],
      "metadata": {
        "id": "91zpVaV--LfA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "while True:\n",
        "    user_input = input(\"You: \")\n",
        "    if user_input.lower() in ['exit', 'quit']:\n",
        "        print(\"Goodbye!\")\n",
        "        break\n",
        "    response = get_response(user_input)\n",
        "    print(f\"Bot: {response}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8AXWrqAY-Q-r",
        "outputId": "a51fb5eb-9932-4d0e-807b-05512724e7d7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "You: Hye give me some product details\n",
            "Bot: Our product is a next-gen AI tool for automation.\n",
            "You: so i dont know how was your day but can you specify thw working hours\n",
            "Bot: We're open from 9 AM to 5 PM, Monday to Friday.\n",
            "You: where is it exactly?\n",
            "Bot: You can reach our support team at support@xyz.com.\n",
            "You: where is your location exactly\n",
            "Bot: Our office is located in New York City.\n",
            "You: hey\n",
            "Bot: Sorry, I didn't understand that.\n",
            "You: hii\n",
            "Bot: Hello! How can I assist you today?\n",
            "You: greetings\n",
            "Bot: Hello! How can I assist you today?\n",
            "You: whats the cost\n",
            "Bot: The pricing starts at $99 per month.\n",
            "You: goodbye\n",
            "Bot: Sorry, I didn't understand that.\n",
            "You: goodbye!\n",
            "Bot: Sorry, I didn't understand that.\n",
            "You: exit\n",
            "Goodbye!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data = {\n",
        "    'Keywords': [\n",
        "        \"Anxiety, worried about any form of result, stress about result, what is going to happen, I don’t know\",\n",
        "        \"jealous, jealousy, anger, hatred, greed, lust, I am angry on him, how do I control anger, jealousy and greed\",\n",
        "        \"heartbreak, how to let go, I cannot let go, he/she left me, breakup, no value of emotion, time-passed with me\",\n",
        "        \"career, success, achievements, recognition, fame, glory, limelight, stardom\"\n",
        "    ],\n",
        "    'Answers': [\n",
        "        \"My dear friend, I understand how tough things are right now. It's completely natural to feel anxious or stressed when you're uncertain about the results. Remember, the Bhagavad Gita teaches us that we have the right to do our duties but not to worry about the results. Focus on your efforts and let go of the outcome. Krishna says, 'You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions' (2:47). Just give it your best shot, and remember that results are influenced by many factors beyond your control. If you need to stay calm, here’s a tip: Embrace your efforts, not the results. Would you like to hear more about finding peace in challenging times?\",\n",
        "        \"My dear friend, feeling anger or jealousy is a common human experience, and it's okay to acknowledge these emotions. According to the Bhagavad Gita, 'While contemplating on the objects of the senses, one develops attachment to them. Attachment leads to desire, and from desire arises anger' (2:62). Try to recognize what’s causing these feelings and remember that they are temporary. Focus on your inner peace rather than the external triggers. Here are a few practical steps to manage these emotions: Take deep breaths, practice mindfulness, and redirect your focus to things that bring you joy. Remember, you have the strength to overcome these feelings. Would you like some more advice on managing emotions?\",\n",
        "        \"My dear friend, I know heartache can be deeply painful. When you’re dealing with a breakup or loss, remember that Krishna said, 'The wise lament neither for the living nor for the dead' (2:11). It’s important to honor your feelings but also to understand that life goes on. Focus on self-care and support from loved ones. Here are some practical tips: Give yourself time to heal, engage in activities you enjoy, and talk to friends or family. Your worth is not defined by this loss. Let’s walk this path together, and remember, brighter days are ahead. Would you like to explore some ways to support yourself during this time?\",\n",
        "        \"My dear friend, concerns about career and success are very common. Krishna advises us not to be attached to the outcomes of our efforts. 'While contemplating on the objects of the senses, one develops attachment to them. Attachment leads to desire, and from desire arises anger' (2:62). Instead of focusing on recognition or fame, concentrate on doing your best in each task. Success is a byproduct of hard work and dedication, not the end goal. Here’s a practical approach: Set personal goals, celebrate small achievements, and stay grounded. Success is a journey, not just a destination. If you want, I can share more on how to stay focused and motivated.\"\n",
        "    ]\n",
        "}"
      ],
      "metadata": {
        "id": "VqGTO33fx7e2"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "from fuzzywuzzy import process\n"
      ],
      "metadata": {
        "id": "vMwTS0u0ByeA"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.DataFrame(data)\n"
      ],
      "metadata": {
        "id": "laYGfkpFB2gu"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kppuEONtB5bK",
        "outputId": "bc32f9b3-6c37-4e5c-adbd-2c0588b018fc"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "                                            Keywords  \\\n",
            "0  Anxiety, worried about any form of result, str...   \n",
            "1  jealous, jealousy, anger, hatred, greed, lust,...   \n",
            "2  heartbreak, how to let go, I cannot let go, he...   \n",
            "3  career, success, achievements, recognition, fa...   \n",
            "\n",
            "                                             Answers  \n",
            "0  My dear friend, I understand how tough things ...  \n",
            "1  My dear friend, feeling anger or jealousy is a...  \n",
            "2  My dear friend, I know heartache can be deeply...  \n",
            "3  My dear friend, concerns about career and succ...  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def get_response(user_input):\n",
        "    best_match = None\n",
        "    best_score = 0\n",
        "    for index, row in df.iterrows():\n",
        "        keywords = row['Keywords'].split(', ')\n",
        "        for keyword in keywords:\n",
        "            match_score = process.extractOne(keyword, user_input.split())\n",
        "            if match_score[1] > best_score:\n",
        "                best_match = row['Answers']\n",
        "                best_score = match_score[1]\n",
        "    if best_score > 70:  # Adjust threshold as needed\n",
        "        # Handle conditional responses\n",
        "        if \"Say yes?\" in best_match:\n",
        "            response = best_match.split(\"Say yes?\")[0]  # Main response\n",
        "            user_response = input(\"Bot: \" + response + \" (Yes/No) \")\n",
        "            if user_response.lower() == 'yes':\n",
        "                additional_info = \"Do your duty, but do not concern yourself with the results. Even while working, give up the pride of doer-ship. Do not be attached to inaction. Think about the process. A result is the byproduct of the process.\"\n",
        "                return response + additional_info\n",
        "            else:\n",
        "                return response\n",
        "        return best_match\n",
        "    else:\n",
        "        return \"Sorry, I didn't understand that.\"\n",
        "\n",
        "while True:\n",
        "    user_input = input(\"You: \")\n",
        "    if user_input.lower() in ['exit', 'quit']:\n",
        "        print(\"Goodbye!\")\n",
        "        break\n",
        "    response = get_response(user_input)\n",
        "    print(f\"Bot: {response}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oqNZSaikB6kF",
        "outputId": "30dd607f-2ac9-4c99-88bd-7176f70306b4"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "You: hey, I want to die what should I do?\n",
            "Bot: My dear friend, I understand how tough things are right now. It's completely natural to feel anxious or stressed when you're uncertain about the results. Remember, the Bhagavad Gita teaches us that we have the right to do our duties but not to worry about the results. Focus on your efforts and let go of the outcome. Krishna says, 'You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions' (2:47). Just give it your best shot, and remember that results are influenced by many factors beyond your control. If you need to stay calm, here’s a tip: Embrace your efforts, not the results. Would you like to hear more about finding peace in challenging times?\n",
            "You: jealous\n",
            "Bot: My dear friend, feeling anger or jealousy is a common human experience, and it's okay to acknowledge these emotions. According to the Bhagavad Gita, 'While contemplating on the objects of the senses, one develops attachment to them. Attachment leads to desire, and from desire arises anger' (2:62). Try to recognize what’s causing these feelings and remember that they are temporary. Focus on your inner peace rather than the external triggers. Here are a few practical steps to manage these emotions: Take deep breaths, practice mindfulness, and redirect your focus to things that bring you joy. Remember, you have the strength to overcome these feelings. Would you like some more advice on managing emotions?\n",
            "You: angry\n",
            "Bot: My dear friend, feeling anger or jealousy is a common human experience, and it's okay to acknowledge these emotions. According to the Bhagavad Gita, 'While contemplating on the objects of the senses, one develops attachment to them. Attachment leads to desire, and from desire arises anger' (2:62). Try to recognize what’s causing these feelings and remember that they are temporary. Focus on your inner peace rather than the external triggers. Here are a few practical steps to manage these emotions: Take deep breaths, practice mindfulness, and redirect your focus to things that bring you joy. Remember, you have the strength to overcome these feelings. Would you like some more advice on managing emotions?\n",
            "You: I loved a girl but she left me\n",
            "Bot: My dear friend, I understand how tough things are right now. It's completely natural to feel anxious or stressed when you're uncertain about the results. Remember, the Bhagavad Gita teaches us that we have the right to do our duties but not to worry about the results. Focus on your efforts and let go of the outcome. Krishna says, 'You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions' (2:47). Just give it your best shot, and remember that results are influenced by many factors beyond your control. If you need to stay calm, here’s a tip: Embrace your efforts, not the results. Would you like to hear more about finding peace in challenging times?\n",
            "You: heartbreak\n",
            "Bot: My dear friend, I know heartache can be deeply painful. When you’re dealing with a breakup or loss, remember that Krishna said, 'The wise lament neither for the living nor for the dead' (2:11). It’s important to honor your feelings but also to understand that life goes on. Focus on self-care and support from loved ones. Here are some practical tips: Give yourself time to heal, engage in activities you enjoy, and talk to friends or family. Your worth is not defined by this loss. Let’s walk this path together, and remember, brighter days are ahead. Would you like to explore some ways to support yourself during this time?\n",
            "You: success and anger\n",
            "Bot: My dear friend, feeling anger or jealousy is a common human experience, and it's okay to acknowledge these emotions. According to the Bhagavad Gita, 'While contemplating on the objects of the senses, one develops attachment to them. Attachment leads to desire, and from desire arises anger' (2:62). Try to recognize what’s causing these feelings and remember that they are temporary. Focus on your inner peace rather than the external triggers. Here are a few practical steps to manage these emotions: Take deep breaths, practice mindfulness, and redirect your focus to things that bring you joy. Remember, you have the strength to overcome these feelings. Would you like some more advice on managing emotions?\n",
            "You: success\n",
            "Bot: My dear friend, concerns about career and success are very common. Krishna advises us not to be attached to the outcomes of our efforts. 'While contemplating on the objects of the senses, one develops attachment to them. Attachment leads to desire, and from desire arises anger' (2:62). Instead of focusing on recognition or fame, concentrate on doing your best in each task. Success is a byproduct of hard work and dedication, not the end goal. Here’s a practical approach: Set personal goals, celebrate small achievements, and stay grounded. Success is a journey, not just a destination. If you want, I can share more on how to stay focused and motivated.\n",
            "You: bye\n",
            "Bot: Sorry, I didn't understand that.\n",
            "You: quit\n",
            "Goodbye!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "N1x1rMD1B-ec"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}