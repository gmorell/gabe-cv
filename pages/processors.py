from pages.models import Page

ENABLED_MODULES = 3

NUMBERS = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
}

def nav_stuff(request):
    all_navs = Page.objects.filter(nav_show=True).order_by('nav_pos')
    nav_left = all_navs.filter(nav_side="l").values('page_slug', 'nav_heading', 'nav_icon', 'nav_side')
    nav_right = all_navs.filter(nav_side="r").values('page_slug', 'nav_heading', 'nav_icon', 'nav_side')
    nav_cnt = all_navs.count()
    
    if nav_cnt + ENABLED_MODULES <= 6: # make three the enabled modules in settings whenever I add that.
        foundation_up = NUMBERS[nav_cnt + ENABLED_MODULES]
    else:
         foundation_up = "six" # until I find something etter
    
    return {"navs_left": nav_left, "navs_right": nav_right, "foundation_up": foundation_up}