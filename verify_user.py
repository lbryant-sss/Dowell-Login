'''
This programs is implemented in django since it has built in login
and authentication functions.
'''
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import render, redirect
from django.contrib.auth import login, authenticate
import re

'''
'''
def languagedetection():
    pass 

def homepage(request):
    form = dowelllogin()
    if not form:
        #100 = login function
        return dowelllogin()
                


def dowelllogin(request):
    # -- Drop down list
        # -- username & check frontend rules of username
        #call language detection
        # -- password &c check password rules
        #take face id
        #take voice
          #list the dropdown thing
        username = request.POST['username']
        password = request.POST['password']
        selfie = request.POST['faceID']
        voice = request.POST['VOICE']
        cancel = request.POST['cancel']
        languagedetection()
        #Username rules
        if not username:
            HttpResponse('Username cannot be empty')
        clean_name = re.search('a-zA-Z', username)
        if not clean_name:
            HttpResponse('Invalid characters.')
        else:
            username = clean_name
        #password rules
        if len(password) < 8:
            HttpResponse('Password must be more than 8 characters.')
            #Ask admin for password and username
        if len(password) > 72:
            HttpResponse('Please use a password less than 72 characters long')
        
        user = authenticate(username=username, password=password)

        if user is not None:
            #check face id
            #if not selfie go to 110 else call dowelllocation()
            if not selfie:
                #110 is the voice processing function
                return dowellvoiceID()
            else:
                dowellconnection(selfie)
                dowellfaceID()
        else:
            #Contact admin for credentials
            return HttpResponse('Request admin for username and password.')
        if cancel:
            return homepage()
        

def dowellvoiceID(request):
    voice = request.POST['voice']
    if not voice:
        #120 is the rights function dowellrights()
        return dowellrights()
    else:
        dowellconnection(voice)
        dowellvoiceID()
        login(request)


def dowellconnection(request):
    pass    

def dowellfaceID(request):
    selfie = request.POST['selfie']
    if not selfie:
        dowellvoiceID()
    else:
        dowellconnection(selfie)
        login(request)




def dowellrights(request):
    #Setting the rights:
    region = request.POST['location']
    country = request.POST['country']
    city = request.POST['city']
    connectivity = request.POST['connectivity']
    device = request.POST['device']
    os = request.POST['os']
    role = request.POST['role']
    process = request.POST['process']
    #if all of these then connect to the master
    #If connected to the master then login
    #Set the rights to an array (list)
    #continue to 200

    if region and country and city:
        if connectivity:
            if device:
                if os:
                    if role:
                        if process:
                            user = authenticate(request)
                            if request.user.has_add_permission(request):
                                if request.user.has_change_permission(request):
                                    if request.user.has_delete_permission(request):
                                        if request.user.has_view_permission(request):
                                            login(request, user)
                                            rights_list = list(region, country, city, connectivity, device, os, role, process)
                                            #200 is the sessions ID function dowellsessions()
                                            return 200
    else:
        HttpResponse('Rights not set. Contact admin for assistance.')

def dowellsessions(request, language, userID, sessionNumber):
    '''
    Create session ID, user ID + lang ID + session number
    call dowellconnection()
    createEvent()
    call results
    dowelllogin(dowelllogin (sessionID, selffie ID, Voice ID, rights (array))																							
'''
    request.session.set(language, userID, sessionNumber)
    return render(request, 'homepage.html', {})