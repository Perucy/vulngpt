import random
import lorem
from decimal import Decimal
import string
import pandas as pd


class TenableRecord():
    keys = ['pluginID', 'severity', 'hasBeenMitigated', 'acceptRisk', 'recastRisk', 'ip', 'uuid', 'port', 'protocol',
            'pluginName', 'firstSeen', 'lastSeen', 'exploitAvailable', 'exploitEase', 'exploitFrameworks', 'synopsis',
            'description', 'solution', 'seeAlso', 'riskFactor', 'stigSeverity', 'vprScore', 'vprContext', 'baseScore',
            'temporalScore', 'cvssVector', 'cvssV3BaseScore', 'cvssV3TemporalScore', 'cvssV3Vector', 'cpe',
            'vulnPubDate', 'patchPubDate', 'pluginPubDate', 'pluginModDate', 'checkType', 'version', 'CVE', 'bid',
            'xref', 'seolDate', 'pluginText', 'dnsName', 'macAddress', 'netbiosName', 'operatingSystem', 'ips',
            'recastRiskRuleComment', 'acceptRiskRuleComment', 'hostUniqueness', 'hostUUID', 'acrScore', 'keyDrivers',
            'assetExposureScore', 'vulnUniqueness', 'vulnUUID', 'uniqueness', 'family', 'repository', 'pluginInfo']

    def __init__(self, cves_lst):
        record = {}

        for key in self.keys:
            if key == 'lastSeen':
                record[key] = TenableRecord.lastSeen(record['firstSeen'])
            elif key == 'exploitEase':
                record[key] = TenableRecord.exploitEase(record['exploitAvailable'])
            elif key == 'vulnPubDate':
                record[key] = TenableRecord.vulnPubDate(record['firstSeen'])
            elif key == 'patchPubDate':
                record[key] = TenableRecord.patchPubDate(record['vulnPubDate'])
            elif key == 'CVE':
                record[key] = TenableRecord.cve(cves_lst)
            else:
                record[key] = getattr(TenableRecord, key)()
        self.record = record

    def pluginID():
        return str(random.randint(10 ** 4, 10 ** 6 - 1))

    def severity():
        choice = random.choice([('4', 'Critical', 'Critical Severity'),
                                ('0', 'Info', 'Informative'),
                                ('3', 'High', 'High Severity'),
                                ('1', 'Low', 'Low Severity'),
                                ('2', 'Medium', 'Medium Severity')])
        return {'id': choice[0], 'name': choice[1], 'description': choice[2]}

    def hasBeenMitigated():
        return str(random.randint(0, 1))

    def acceptRisk():
        return '0'

    def recastRisk():
        return '0'

    def ip():
        return ".".join(map(str, (random.randint(0, 255)
                                  for _ in range(4))))

    def uuid():
        import uuid as uid
        return str(uid.uuid4())

    def port():
        return str(random.randint(1, 10 ** 6 - 1))

    def protocol():
        return random.choice(['UDP', 'TCP', 'ICMP'])

    def pluginName():
        return None

    def firstSeen():
        return str(random.randint(10 ** 9, 10 ** 11 - 1))

    def lastSeen(first):
        # has to occur after firstSeen
        return str(random.randint(int(first), 10 ** 11 - 1))

    def exploitAvailable():
        return random.choice(['No', 'Yes'])

    def exploitEase(exploit):
        # if exploitAvailable is none then no ease
        if exploit == 'No':
            return random.choice(['', 'No known exploits are available'])
        return random.choice(['Exploits are available', 'No exploit is required'])

    def exploitFrameworks():
        # Ignoring this as we won't use
        return None

    def synopsis():
        # Short description of vuln
        return lorem.sentence()

    def description():
        # description of vuln
        return lorem.paragraph()

    def solution():
        return lorem.sentence()

    def seeAlso():
        # Reference urls
        return None

    def riskFactor():
        return random.choice(['Medium', 'High', 'Low', 'None', 'Critical'])

    def riskFactor():
        return random.choice(['', 'II', 'III', 'I'])

    def stigSeverity():
        return None

    def vprScore():
        return str(round(Decimal(random.random() * 10), 1))

    def vprContext():
        # ignoring for now as complex
        return None

    def baseScore():
        return str(round(Decimal(random.random() * 10), 1))

    def temporalScore():
        return str(round(Decimal(random.random() * 10), 1))

    def cvssVector():
        # ignoring for now
        return None

    def cvssV3BaseScore():
        return str(round(Decimal(random.random() * 10), 1))

    def cvssV3TemporalScore():
        return str(round(Decimal(random.random() * 10), 1))

    def cvssV3Vector():
        # ignoring for now
        return None

    def cpe():
        # ignoring for now
        return None

    def vulnPubDate(first):
        # must occur before firstSeen
        return str(random.randint(10 ** 9, int(first)))

    def patchPubDate(pub):
        # has to occur after vulnPubDate
        return str(random.randint(int(pub), 10 ** 11 - 1))

    def pluginPubDate():
        # ignoring for now
        return None

    def pluginModDate():
        # ignoring for now
        return None

    def checkType():
        # ignoring for now
        return None

    def version():
        # ignoring for now
        return None

    def cve(cves_lst):

        return random.choice(cves_lst)

    def bid():
        # ignoring for now
        return None

    def xref():
        # ignoring for now
        return None

    def version():
        # ignoring for now
        return None

    def seolDate():
        # ignoring for now
        return None

    def pluginText():
        # ignoring for now
        return None

    def dnsName():
        subdomain = random.choice(['',
                                   'perseus.tufts.edu',
                                   'tusk.tufts.edu',
                                   'hrilab.tufts.edu',
                                   'openit',
                                   'fletcher.tufts.edu',
                                   'admin.tufts.edu',
                                   'ad.tufts.edu',
                                   'moit.tufts.edu',
                                   'studentservices.tufts.edu',
                                   'echo360.tufts.edu',
                                   'cabot205crestrontp.tufts.edu',
                                   'ase.tufts.edu',
                                   'net.tufts.edu',
                                   'uit.tufts.edu',
                                   'grafton.tufts.edu',
                                   'cee.tufts.edu',
                                   'first-dsx.app',
                                   'tccs.tufts.edu',
                                   'lib.tufts.edu',
                                   'nutrition.tufts.edu',
                                   'hr.tufts.edu',
                                   'phy.tufts.edu',
                                   'engineering.tufts.edu',
                                   'admissions.tufts.edu',
                                   'publicsafety.tufts.edu',
                                   'boston.tufts.edu',
                                   'it.tufts.edu',
                                   'medford.tufts.edu',
                                   'operations.tufts.edu',
                                   'chem.tufts.edu',
                                   'hsl.tufts.edu',
                                   'vet.tufts.edu',
                                   'hnrc.tufts.edu',
                                   'as.tufts.edu',
                                   'orgs.tufts.edu',
                                   'awre-softball-camera.tufts.edu',
                                   'viceprovost.tufts.edu',
                                   'hnrcdocs',
                                   'ut.tufts.edu',
                                   'infonet.tufts.edu',
                                   'dental.tufts.edu',
                                   'med.tufts.edu',
                                   'psy.tufts.edu',
                                   'iut.tufts.edu',
                                   'awre-softball-access-point.tufts.edu',
                                   'wc.tufts.edu',
                                   'advancement.tufts.edu',
                                   'library.tufts.edu'])
        nm = ''.join([random.choice(string.ascii_letters) for i in range(10)])
        return nm + '.' + subdomain

    def macAddress():
        return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255),
                                            random.randint(0, 255),
                                            random.randint(0, 255))

    def netbiosName():
        # ignoring for now
        return None

    def operatingSystem():
        # ignoring for now
        return None

    def ips():
        # ignoring for now
        return None

    def recastRiskRuleComment():
        # ignoring for now
        return None

    def acceptRiskRuleComment():
        # ignoring for now
        return None

    def hostUniqueness():
        # ignoring for now
        return None

    def hostUUID():
        # ignoring for now
        return None

    def acrScore():
        return None

    def keyDrivers():
        return None

    def vulnUUID():
        return None

    def assetExposureScore():
        return ''

    def vulnUniqueness():
        # ignoring for now
        return None

    def uniqueness():
        # ignoring for now
        return None

    def family():
        # ignoring for now
        return None

    def repository():
        # ignoring for now
        return None

    def pluginInfo():
        # ignoring for now
        return None
if __name__ == "__main__":
    import json

    df = pd.read_csv('New_Vuln_Notification_Coding.csv')
    cves = df['CVE'].dropna().tolist()
    cve_lst = list(set(cves))
    cves_lst = [f"CVE-{cve}" if not cve.startswith("CVE-") else cve for cve in cve_lst]

    data = [TenableRecord(cves_lst).record for i in range(100)]

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


