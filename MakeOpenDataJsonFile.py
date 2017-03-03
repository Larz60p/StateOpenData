import json


class MakeOpenDataJSON:
    def __init__(self):
        self.jfilename = 'StateOpenData.JSON'
        self.OpenData = {
            'Alabama': {
                'state': 'http://open.alabama.gov/'
            },
            'Alaska': {
                'state': 'None',
                'DeptNaturalResources': 'http://www.asgdc.state.ak.us/'
            },
            'Arizona': {
                'state': 'https://ptl.az.gov/app/transparency/index.html'
            },
            'Arkansas': {
                'state': 'http://transparency.arkansas.gov/'
            },
            'California': {
                'state': 'https://data.ca.gov/',
                'San Diego': 'http://data.sandiego.gov/',
                'San Francisco': 'https://data.sfgov.org/'
            },
            'Colorado': {
                'state': 'https://www.colorado.gov/data/'
            },
            'Connecticut': {
                'state': 'https://data.ct.gov/'
            },
            'Delaware': {
                'state': 'https://data.delaware.gov/',
                'topics': 'http://delaware.gov/topics/data.shtml',
            },
            'District Of Columbia': {
                'state': 'http://opendata.dc.gov/'
            },
            'Florida': {
                'state': 'http://geodata.myflorida.com/',
                'Right To Know': 'http://floridahasarighttoknow.myflorida.com/'
            },
            'Georgia': {
                'state': 'http://www.open.georgia.gov/'
            },
            'Hawaii': {
                'state': 'https://data.hawaii.gov/',
                'Honolulu Land Information System': 'http://gis.hicentral.com/'
            },
            'Idaho': {
                'state': 'http://data.gis.idaho.gov/'
            },
            'Illinois': {
                'state': 'https://data.illinois.gov/',
                'South Suburban Mayors and Managers': 'https://data.illinois.gov/ssmma'
            },
            'Indiana': {
                'state': 'http://www.stats.indiana.edu/'
            },
            'Iowa': {
                'state': 'https://data.iowa.gov/'
            },
            'Kansas': {
                'state': 'http://www.kansas.gov/KanView/'
            },
            'Kentucky': {
                'state': 'http://opendoor.ky.gov/Pages/default.aspx'
            },
            'Louisiana': {
                'state': 'https://wwwcfprd.doa.louisiana.gov/latrac/portal.cfm'
            },
            'Maine': {
                'state': 'https://data.maine.gov/'
            },
            'Maryland': {
                'state': 'https://data.maryland.gov/'
            },
            'Massachusetts': {
                'state': 'http://massbigdata.org/data/the-massachusetts-open-data-catalog/',
                'Boston': 'https://data.cityofboston.gov/',
                'Cambridge': 'https://data.cambridgema.gov/',
                'Framingham': 'http://www.civicdashboards.com/city/framingham-ma-16000US2524960/'
            },
            'Michigan': {
                'state': 'https://data.michigan.gov/'
            },
            'Minnesota': {
                'state': 'http://mn.gov/portal/'
            },
            'Mississippi': {
                'state': 'https://www.arcgis.com/home/item.html?id=a266920482b7486baac8f591a63f19a4'
            },
            'Missouri': {
                'state': 'https://data.mo.gov/'
            },
            'Montana': {
                'state': 'https://data.datamontana.us/browse'
            },
            'Nebraska': {
                'state': 'http://www.nebraska.gov/'
            },
            'Nevada': {
                'state': 'http://open.nv.gov/'
            },
            'New Hampshire': {
                'state': 'https://www.nh.gov/doit/open-source/'
            },
            'New Jersey': {
                'state': 'https://data.nj.gov/'
            },
            'New Mexico': {
                'state': 'http://www.sunshineportalnm.com/'
            },
            'New York': {
                'state': 'https://nycopendata.socrata.com/',
                'NY Dept Of Health': 'https://health.data.ny.gov/'
            },
            'North Carolina': {
                'state': 'https://open-nc.org/',
                'Asheville': 'http://data.ashevillenc.gov/',
                'Cary': 'https://data.townofcary.org/page/home/',
                'Chapel Hill': 'https://www.chapelhillopendata.org/explore/',
                'Charlotte': 'http://clt-charlotte.opendata.arcgis.com/',
                'Durham': 'https://opendurham.nc.gov/page/home/',
                'Fayetteville': 'http://data.fayettevillenc.gov/',
                'Greensboro': 'https://data.greensboro-nc.gov/',
                'Raleigh': 'https://localwiki.org/raleigh/Open_Data_Sources',
                'WakeCounty': 'http://data-wake.opendata.arcgis.com/',
                'GISresources': 'http://www.cgia.state.nc.us/dataresources.aspx',
                'Mecklenburg Open Mapping': 'http://maps.co.mecklenburg.nc.us/openmapping/',
                'OpenDataInstitute Of NC': 'https://www.slideshare.net/TheODINC',
                'State Data Center NC OSBM': 'https://www.osbm.nc.gov/facts-figures/state-data-center'
            },
            'North Dakota': {
                'state': 'None',
                'GIS North Dakota ITD': 'https://www.nd.gov/itd/statewide-alliances/gis'
            },
            'Ohio': {
                'state': 'http://www.ohio.gov/government/transparency/'
            },
            'Oklahoma': {
                'state': 'https://www.ok.gov/about/data.html'
            },
            'Oregon': {
                'state': 'https://data.oregon.gov/'
            },
            'Pennsylvania': {
                'state': 'https://data.pa.gov/',
                'Phidelphia': 'https://www.opendataphilly.org/'
            },
            'Rhode Island': {
                'state': 'http://www.ri.gov/data/'
            },
            'South Carolina': {
                'state': 'http://www.gis.sc.gov/'
            },
            'South Dakota': {
                'state': 'http://open.sd.gov/'
            },
            'Tennessee': {
                'state': 'http://tn.gov/transparenttn'
            },
            'Texas': {
                'state': 'https://data.texas.gov/'
            },
            'Utah': {
                'state': 'https://www.utah.gov/data/'
            },
            'Vermont': {
                'state': 'https://data.vermont.gov/'
            },
            'Virginia': {
                'state': 'https://data.virginia.gov/'
            },
            'Washington': {
                'state': 'https://data.wa.gov/'
            },
            'West Virginia': {
                'state': 'None',
                'Civic Dashboard': 'http://catalog.opendata.city/dataset?license_id=odc-by&tags=West+Virginia',
                'Map West Virginia': 'http://www.mapwv.gov/help-gisdata.php'
            },
            'Wisconsin': {
                'state': 'None',
                'Madison': 'https://data.cityofmadison.com/'
            },
            'Wyoming': {
                'state': 'None',
                'National And Community Service': 'https://data.nationalservice.gov/Volunteering-and-Civic-Engagement/Wyoming/bpid-mwn8/data'
            }
        }
        self.make_file()

    def make_file(self):
        with open(self.jfilename, "w") as f:
            json.dump(self.OpenData, f)


if __name__ == '__main__':
    MakeOpenDataJSON()
