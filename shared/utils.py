def get_lang_code(request):
    lang_codes = ['uz', 'en', 'ru']
    lang_code = request.GET.get('lang')
    if lang_code not in lang_codes:
        lang_code = 'uz'
    return {"lang_code":lang_code}