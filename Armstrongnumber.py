{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Armstrongnumber.py",
      "provenance": [],
      "authorship_tag": "ABX9TyMVkgwL1XOoDKEWVGWFJO/6",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
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
        "<a href=\"https://colab.research.google.com/github/Onurx35/python-project/blob/main/Armstrongnumber_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V-rksyLH2p_q",
        "outputId": "4a8d2311-bbe9-4707-8bc4-540ccbab6a55"
      },
      "source": [
        "while True:\n",
        "  num = input(\"Please enter a positive number: \")\n",
        "  digits = len(num)\n",
        "  summ = 0\n",
        "  if not num.isdigit():\n",
        "    print(num, \"is invalid entry. Please enter a numeric value.\")\n",
        "  elif int(num) >= 0:\n",
        "    for i in range(digits):\n",
        "      summ += int(num[i]) ** digits\n",
        "    if summ == int(num):\n",
        "      print(num, \"is an Armstrong number\")\n",
        "      break\n",
        "    else:\n",
        "      print(num, \"is not Armstrong number\")\n",
        "      break"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Please enter a positive number: 9839481\n",
            "9839481 is not Armstrong number\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
