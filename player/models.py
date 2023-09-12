from django.db import models
from dataclasses import dataclass

BASE_URL = 'http://localhost:3000/static'
TRACK_LINKS = {
  'טל אנגרט  -   מאפייני הקיוםBeLateral .mp3': f'{BASE_URL}/טל אנגרט  -   מאפייני הקיוםBeLateral .mp3',
  'טל אנגרט  -  פעולה אנושית משותפת  BeLateral.mp3': f'{BASE_URL}/טל אנגרט  -  פעולה אנושית משותפת  BeLateral.mp3',
  'אסף פדרמן - 15 דק סריקת גוף BeLateral.mp3': f'{BASE_URL}/אסף פדרמן - 15 דק סריקת גוף BeLateral.mp3'
}
