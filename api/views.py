from django.shortcuts import render
import requests

def github(request):
    repos_url = 'https://api.github.com/search/repositories?q=created:>2021-07-19&sort=stars&order=desc'
    repos_results = requests.get(repos_url).json()
    language = []
    for repo in repos_results["items"][0:3]:
        language_url = f'https://api.github.com/search/repositories?q=language:{repo["language"]}&sort=forks&order=desc'
        language_results = requests.get(language_url).json()
        language.append({'name': repo["language"], 'count': language_results["total_count"]})
        
    return render(request, 'core/github.html', {'data': language})