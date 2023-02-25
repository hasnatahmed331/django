from django.shortcuts import render ,HttpResponse
from django.conf import settings
from django.shortcuts import redirect 
import msal
from django.urls import reverse

def azure_ad_b2c_login(request):
    # authority=f"https://fullfrme.b2clogin.com/fullfrme.onmicrosoft.com/{settings.AZURE_AD_B2C_SIGN_IN_POLICY}"
    # client_app = msal.PublicClientApplication(settings.AZURE_AD_B2C_CLIENT_ID, authority=authority)

    # # Use MSAL to generate the authorization request URL
    # auth_url = client_app.get_authorization_request_url(
    #     scopes=settings.AZURE_AD_B2C_SCOPES,
    #     redirect_uri=request.build_absolute_uri(reverse('azure_ad_b2c_callback')),
    # )

    # # Redirect the user to the authorization request URL
    # return redirect(auth_url)
    return HttpResponse("welcome")

def azure_ad_b2c_callback(request):
    # authority=f"https://fullfrme.b2clogin.com/fullfrme.onmicrosoft.com/{settings.AZURE_AD_B2C_SIGN_IN_POLICY}"
    # client_app = msal.PublicClientApplication(settings.AZURE_AD_B2C_CLIENT_ID, authority=authority)

    # # Use MSAL to exchange the authorization code for an access token
    # result = client_app.acquire_token_by_authorization_code(
    #     request.GET.get('code'),
    #     scopes=settings.AZURE_AD_B2C_SCOPES,
    #     redirect_uri=request.build_absolute_uri(reverse('azure_ad_b2c_callback')),
    # )

    # # Render a template to display the access token
    # return render(request, 'azure_ad_b2c_callback.html', {'access_token': result['access_token']})
    return HttpResponse("hello")