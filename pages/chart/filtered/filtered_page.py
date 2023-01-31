from pages.chart.branches_func import BranchesFunction
from pages.chart.chart_page import ChartPage

class FilteredPage(ChartPage, BranchesFunction):
    def __init__(self, *args, **kwargs):
        super(FilteredPage, self).__init__(*args, **kwargs)
