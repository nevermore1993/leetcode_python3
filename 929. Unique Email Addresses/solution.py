def numUniqueEmails(emails: 'List[str]'):
    result = set()
    for email in emails:
        index_at = email.index("@")
        if email.find("+") != -1:
            index_plus = email.index("+")
            if (index_plus < index_at):
                email = email[:index_plus] + email[index_at:]
        index_at = email.index("@")
        while True:
            index_dot = email.index(".")
            if (index_dot < index_at):
                email = email[:index_dot] + email[index_dot+1:]
                index_at = email.index("@")
            else:
                break
        result.add(email)
    return len(result)

s = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(s))



def numUniqueEmails(self, emails: 'List[str]') -> 'int':
    emails_set = set()
    for email in emails:
        [temp_local_name, domain_name] = email.split('@')
        [tmp_local_name, a, b] = temp_local_name.partition('+')
        local_name = tmp_local_name.replace('.', '')
        fixed_email = local_name + '@' + domain_name
        emails_set.add(fixed_email)
    return len(emails_set)
    
