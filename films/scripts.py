from films.models import *
import xlrd

def import_from_xlsx(file_location):
    objects = []
    workbook = xlrd.open_workbook(file_location)
    for name in workbook.sheet_names():
        sheet = workbook.sheet_by_name(name)
        headings = sheet.row(0)
        for num in range(1,sheet.nrows):
            obj = {}
            for num, cell in enumerate(sheet.row(num)):
                if not headings[num].value:
                    continue
                label = headings[num].value
                if cell.value and cell.value != "":
                    obj[label] = cell.value
            objects.append(obj)
    return objects


def save_obj(obj):
    film = Film.objects.get_or_create(title=obj['Title'])[0]
    if 'Series' in obj:
        film.series = Series.objects.get_or_create(name=obj['Series'])[0]
    if 'tags' in obj:
        for t in obj['tags'].split(','):
            if t == "" or t == " ":
                continue
            tag = Tag.objects.get_or_create(name=t)
            film.tags.add(tag[0])
    if 'Production Company' in obj:
        film.production_company = ProductionCompany.objects.get_or_create(name=obj['Production Company'])[0]

    if 'Do We Have?' in obj and obj['Do We Have?'].lower() in ['yes']:
        film.have_it = True

    if 'Original distributor' in obj:
        film.current_distributor = Distributor.objects.get_or_create(name=obj['Original distributor'])[0]
    if 'Current distributor' in obj:
        film.original_distributor = Distributor.objects.get_or_create(name=obj['Current distributor'])[0]
    if 'Release Date' in obj:
        try:
            film.release_date = datetime.datetime.strptime(obj['Release Date'], "%m/%d/%Y").date()
        except:
            try:
                film.release_date = datetime.datetime.strptime(obj['Release Date'], "%m/%d/%y").date()
            except:
                print obj['Release Date']
    if 'Year' in obj:
        film.year = int(obj['Year'])

    if 'Work Notes' in obj:
        film.work_notes = obj['Work Notes']
    if 'Description/History' in obj:
        film.description = obj['Description/History']

    if 'Run Time' in obj:
        try:
            film.duration = obj['Run Time']
        except:
            print "RUNTIME", obj['Run Time']

    if 'Copyright status' in obj:
        film.copyright_status = obj['Copyright status']
    if 'Copyright status source' in obj:
        film.copyright_status_source = obj['Copyright status source']    
    if 'Copyright claimant' in obj:
        film.copyright_claimant = obj['Copyright claimant']

    film.save()
    return film


