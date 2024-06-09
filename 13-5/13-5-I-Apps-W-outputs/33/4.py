
def solve(s):
    ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if s < 10:
        return ones[s]
    elif s < 20:
        return teens[s - 10]
    elif s < 100:
        return tens[s // 10 - 2] + ('-' + ones[s % 10] if s % 10 != 0 else '')
    else:
        return ones[s // 100] + '-hundred' + ('-' + solve(s % 100) if s % 100 != 0 else '')

