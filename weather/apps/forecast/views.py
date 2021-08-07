from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny
from django.http import HttpResponse
from rest_framework.views import APIView
import json
from datetime import datetime
from weather.settings import stageSetted, DEBUG
import os
import logging

from bs4 import BeautifulSoup
import requests

logFormatter = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format=logFormatter, level=logging.INFO)
logger = logging.getLogger(__name__)


class WeatherRetrieveAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        # if(DEBUG):
        #     logger.info(os.environ)
            
        """[Request data from climatempo URL]

        Returns:
            [type]: [request URL]
        """
        msg = requests.get('https://www.climatempo.com.br/previsao-do-tempo/cidade/321/riodejaneiro-rj')
        msg.encoding = 'UTF-8'
        soup = BeautifulSoup(msg.text, 'html.parser')
        
        # print(soup.find(id='min-temp-1').string)
        
        resume = soup.find(class_='-gray -line-height-24 _center').text
        
        tempMin = soup.find(id='min-temp-1').text
        tempMax = soup.find(id='max-temp-1').text
        resume = resume.replace('\n\n\n\n', ' -')
        format_resume = resume.split('\n')
        resume_text = ''

        for x in format_resume:
            if x != '':
                resume_text = resume_text + x + ' '
                
        return HttpResponse(json.dumps({
            "Resumo": resume_text,
            "Temperatura mínima": tempMin,
            "Temperatura máxima": tempMax
        }, indent=3, ensure_ascii=False), status=status.HTTP_200_OK, content_type='application/json')
