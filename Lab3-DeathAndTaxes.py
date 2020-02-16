def is_valid(status,income):
    if (status=='single' or status=='married filing jointly' or status=='married filing separately' or status=='widow' or status=='widower' or status=='head of household') and (int(income)>=0):
        print('True')
        return True
    else:
        print('False')
        return False
is_valid('single',2000)
def get_tax(status,income):
    if is_valid:
        tax=0
        if status=='single':
            if (income>=0) and (income<=9325):
                tax=(.1*income)
            elif (income>=9326) and (income<=37950):
                tax=(.1*(9325-0))+(.15*(income-9325))
            elif (income>=37951) and (income<=91900):
                tax=(.1*(9325-0))+(.15*(37951-9325))+(.25*(income-37951))
            elif (income>=91901) and (income<=191650):
                tax=((.1*(9325-0))+(.15*(37951-9325))+(.25*(91901-37950))+(.28*(income-91901)))
            elif (income>=191651) and (income<=416700):
                tax=((.1*(9325-0))+(.15*(37951-9325))+(.25*(91901-37950))+(.28*(191651-91901))+(.33*(income-191651)))
            elif (income>=416701) and (income<=418400):
                tax=((.1*(9325-0))+(.15*(37951-9325))+(.25*(91901-37950))+(.28*(191651-91901)+(.33*(416701-191651))+(.35*(income-416701))))
            else:
                 tax=((.1*(9325-0))+(.15*(37951-9325))+(.25*(91901-37950))+(.28*(191651-91901)+(.33*(416701-191651))+(.35*(418401-416701))+(.396*(income-418401))))
        elif status=='marries filing jointly' or status=='widow' or status=='widower':
            if (income>=0) and (income<=18650):
                tax=(.1*income)
            elif (income>=18651) and (income<=75900):
                tax=(.1*(18651-0))+(.15*(income-18651))
            elif (income>=75901) and (income<=153100):
                tax=(.1*(18651-0))+(.15*(75900-18651))+(.25*(income-75901))
            elif (income>=153101) and (income<=233350):
                     tax=(.1*(18651-0)+(.15*75900-18651)+(.25*153101-75901)+(.28*(income-153101)))
            elif (income>=233351) and (income<=416700):
                     tax=((.1*(18651-0))+(.15*(75901-18651))+(.25*(153101-75901))+(.28*(233351-153101))+(.33*(income-233351)))
            elif (income>=416701) and (income<=418400):
                     tax=((.1*(18651-0))+(.15*(75901-18651))+(.25*(153101-75901))+(.28*(233351-153101)+(.33*(416701-233351))+(.35*(income-416701))))
            else:
                    tax=((.1*(18651-0))+(.15*(75901-18651))+(.25*(153101-75901))+(.28*(233351-153101)+(.33*(416701-191651))+(.35*(416701-470700))+(.396*(income-470701))))
        elif status=='married filing separately':
            if (income>=0) and (income<=9325):
                tax=(.1*income)
            elif (income>=9326) and (income<=37950):
                tax=(.1*(9326-0)+(.15*income-9326))
            elif (income>=37951) and (income<=76550):
                tax=(.1*(9326-0))+(.15*(37951-9326))+(.25*(income-37951))
            elif (income>=76551) and (income<=116675):
                     tax=(.1*(9326-0))+(.15*(37951-9326))+(.25*(76551-37951))+(.28*(income-76551))
            elif (income>=116676) and (income<=208350):
                     tax=((.1*(9326-0))+(.15*(37951-9326))+(.25*(76551-37951))+(.28*(116676-76551))+(.33*(income-116676)))
            elif (income>=208351) and (income<=235350):
                     tax=((.1*(9326-0))+(.15*(37951-9326))+(.25*(76551-37951))+(.28*(116676-76551))+(.33*(208351-116676))+(.35*(income-208351)))
            else:
                    tax=((.1*(9326-0))+(.15*(37951-9326))+(.25*(76551-37951))+(.28*(116676-76551))+(.33*(208351-116676))+(.35*(235351-208351))+(.396*(income-235351)))
        else:
            if (income>=0) and (income<=13350):
                tax=(.1*income)
            elif (income>=13351) and (income<=50800):
                tax=(.1*(13351-0))+(.15*(income-13351))
            elif (income>=50801) and (income<=131200):
                tax=(.1*(13351-0))+(.15*(50801-13351))+(.25*(income-50801))
            elif (income>=131201) and (income<=212500):
                     tax=(.1*(13351-0))+(.15*(50801-13351))+(.25*(131201-50801))+(.28*(income-131201))
            elif (income>=212501) and (income<=416700):
                     tax=((.1*(13351-0))+(.15*(50801-13351))+(.25*(131201-50801))+(.28*(212501-50801))+(.33*(income-212501)))
            elif (income>=416701) and (income<=444500):
                     tax=((.1*(13351-0))+(.15*(50801-13351))+(.25*(131201-50801))+(.28*(212501-50801))+(.33*(416701-212501))+(.35*(income-416701)))
            else:
                    tax=((.1*(13351-0))+(.15*(50801-13351))+(.25*(131201-50801))+(.28*(212501-50801)+(.33*(416701))+(.35*(444501-416701))+(.396*(income-444501))))
    return tax
def percent_of_income(tax,income):
    return (int(tax)/int(income))*100
    print('Percent of Income:',percent_of_income(tax,income),'%')

def main_function(status,income):
    print(get_tax(status,income))
    print(percent_of_income(get_tax(status,income),income))
    return
main_function('single',50000)
                 




