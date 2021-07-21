from django.shortcuts import render
from . import scrapping, scrappingWebsiteOnly

# Create your views here.
def home_view(request):
  print(request.user)
  getCompanyName = request.POST.get('company_name')
  print(getCompanyName)
  
  url, contact_url = scrapping.getSearchURL(getCompanyName)
  company_url = scrapping.getCompanyURL(url)
  company_contact_url = scrapping.getCompanyURL(contact_url)
  phoneList, emailList = scrapping.getPhoneAndEmail(company_contact_url)
  linkedin_url, title = scrapping.getCEO(getCompanyName)

  dictionary = {'companyName': getCompanyName, 'url': url, 'contact_url': contact_url,
                'company_url': company_url, 'company_contact_url': company_contact_url,
                'phoneList': phoneList, 'emailList': emailList,
                'linkedin_url': linkedin_url, 'title': title,}
 
  return render(request, "index.html", dictionary)

def multiple_inputView(request):
  print(request.user)
  nCompanies = 4    # change here to change the number of input companies
  numberList = [i for i in range(1, nCompanies+1)]  # numbers --> 1, 2, 3...

  romanNumberList = []  # roman numbers --> 1st, 2nd, 3rd...
  r2 = [str(i)+"th" for i in range(4, nCompanies+1)]
  r1 = ['1st', '2nd', '3rd',]
  if nCompanies >= 4:
    for i in range(len(r2)):
      romanNumberList2 = [r1, r2]
    romanNumberList = [n for lists in romanNumberList2 for n in lists]
  else:
    for i in range(nCompanies):
      romanNumberList.append(r1[i])  
  
  getCompanyName = [request.POST.get('companyName'+str(i)) for i in romanNumberList]
 
  #print(getCompanyName)
  
  companyUrls = []
  phones = []
  emails = []
  linkedinUrls = []
  titles = []
  for name in getCompanyName:
    url, contact_url = scrapping.getSearchURL(name)

    companyUrl = scrapping.getCompanyURL(url)
    company_contact_url = scrapping.getCompanyURL(contact_url)

    companyUrls.append(companyUrl)
    
    linkedin_url, title = scrapping.getCEO(name)
    linkedinUrls.append(linkedin_url)
    titles.append(title)

    phoneList, emailList = scrapping.getPhoneAndEmail(company_contact_url)

    phones.append(phoneList)
    emails.append(emailList)

  dictionary = {'numberList': numberList, 'romanNumberList': romanNumberList,
                'companyUrls': companyUrls, 'linkedinUrls': linkedinUrls,
                'titles': titles, 'phones': phones, 'emails': emails,
                'company_name': getCompanyName,}
  return render(request, "multiple.html", dictionary)  

# to display only company website only:
def home_viewWebsite(request):
  print(request.user)
  nCompanies = 7  # change here to change the number of input companies
  numberList = [i for i in range(1, nCompanies+1)]  # numbers --> 1, 2, 3...

  romanNumberList = []  # roman numbers --> 1st, 2nd, 3rd...
  r2 = [str(i)+"th" for i in range(4, nCompanies+1)]
  r1 = ['1st', '2nd', '3rd',]
  if nCompanies >= 4:
    for i in range(len(r2)):
      romanNumberList2 = [r1, r2]
    romanNumberList = [n for lists in romanNumberList2 for n in lists]
  else:
    for i in range(nCompanies):
      romanNumberList.append(r1[i])  
  
  getCompanyName = [request.POST.get('companyName'+str(i)) for i in romanNumberList]
 
  #print(getCompanyName)
  
  companyUrls = []

  for name in getCompanyName:
    url, contact_url = scrappingWebsiteOnly.getSearchURL(name)

    companyUrl = scrappingWebsiteOnly.getCompanyURL(url)

    companyUrls.append(companyUrl)
    

  dictionary = {'numberList': numberList, 'romanNumberList': romanNumberList,
                'companyUrls': companyUrls, 'company_name': getCompanyName,}
  return render(request, "indexWebsite.html", dictionary)