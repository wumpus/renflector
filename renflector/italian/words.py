def prepare_dict():
    # comments, maybe end of line
    # blank lines
    # u/v equivalent; i/j equivalent
    # no html entities: require utf8 instead; NFC
    # be robust against iso-8859-1 (latin-1) or other non-utf8
    # syntax check of entries with irregulars to see if they're complete
    pass


def expand_word():
    # output word table: string, part of speech, gender, number, definition
    # "spelling rules" (postpass?)
    # noun
    # adjective
    # verb
    # article
    # adverb
    # preposition
    # interjection
    # conjunction
    # pronoun
    # abbreviation -- treat as alt spelling?
    # negri abbreviation -- treat as alt spelling?
    pass


def expand_noun(word):
    noun_rules = {
        '-a': [['-a', 'N fem sing'], ['-e', 'N fem plural']],
        '-o': [['-o', 'N masc sing'], ['-i', 'N masc plural']],
        '-e': [['-e', 'N either sing'], ['-i', 'N either plural']],
    }
    spelling_rules = {
        '-ce': 'che',
        '-ge': 'ghe',
        '-ci': 'chi',
        '-gi': 'ghi',
    }


def expand_adjective(word):
    # expect all adjectives to arrive ending with -a ???
    adj_rules = {
        '-a': [['-a', 'Adj fem sing'], ['-e', 'Adj fem plural']],
        '-o': [['-o', 'Adj masc sing'], ['-i', 'Adj masc plural']],
        '-e': [['-e', 'Adj either sing'], ['-i', 'Adj either plural']],
    }
    adverb_rules = {
        # [aeio][lr]e drop the e before adding -mente
        # else just tack on mente
    }

def expand_verb(word):
    # expect all verbs to arrive ending with -are ???
    verb_rules = {
        '-are': [
            ['-o', 'verb I'],
            ['-i', 'verb you/sing'],
            ['-a', 'verb he/hse/it'],
            ['-iamo', 'verb we'],
            ['-ate', 'verb you/pl'],
            ['-ano', 'verb they'],

            ['-ando', 'gerund'],
            ['-andomi', 'gerund me'],
            ['-andolo', 'gerund him'],
            ['-andoli', 'gerund him/pl'],
            ['-andola', 'gerund her'],
            ['-andole', 'gerund her/pl '],
            ['-andosi', 'gerund -ing + him/her/themselves'],

            ['-ante', 'pres. part. -ing sing ??'],
            ['-anti', 'pres. part. -ing pl ??'],

            ['-ando', 'pres. part. -ing masc ??'],
            ['-ato', 'past part. -ing masc'],
            ['-anda', 'pres. part. -ing fem'],
            ['-ata', 'past part. -ing fem'],

            # usually -are verbs switch to -er in the future
            ['-er&ograve', 'verb future I'],
            ['-erai', 'verb future you/sing'],
            ['-er&agrave;', 'verb future s/he'],
            ['-eremo', 'verb future we'],
            ['-erete', 'verb future you/pl'],
            ['-eranno', 'verb future they'],

            # but sometimes they don't, so ...
            ['-ar&ograve', 'verb future I (extra)'],
            ['-arai', 'verb future you/sing (extra)'],
            ['-ar&agrave;', 'verb future s/he (extra)'],
            ['-aremo', 'verb future we (extra)'],
            ['-arete', 'verb future you/pl (extra)'],
            ['-aranno', 'verb future they (extra)'],
        ],
        '-ere': [
            ['-o', 'verb I'],
            ['-i', 'verb you/sing'],
            ['-e', 'verb he/hse/it'],
            ['-iamo', 'verb we'],
            ['-ete', 'verb you/pl'],
            ['-ono', 'verb they'],

            ['-endo', 'gerund'],
            ['-endomi', 'gerund me'],
            ['-endolo', 'gerund him'],
            ['-endoli', 'gerund him/pl'],
            ['-endola', 'gerund her'],
            ['-endole', 'gerund her/pl '],
            ['-endosi', 'gerund -ing + him/her/themselves'],

            ['-ente', 'pres. part. -ing sing ??'],
            ['-enti', 'pres. part. -ing pl ??'],

            ['-endo', 'pres. part. -ing masc ??'],
            ['-uto', 'past part. -ing masc'],
            ['-enda', 'pres. part. -ing fem'],
            ['-uta', 'past part. -ing fem'],

            ['-er&ograve', 'verb future I'],
            ['-erai', 'verb future you/sing'],
            ['-er&agrave;', 'verb future s/he'],
            ['-eremo', 'verb future we'],
            ['-erete', 'verb future you/pl'],
            ['-eranno', 'verb future they'],
        ],
        '-ire': [
            ['-${isc}o', 'verb I'],
            ['-${isc}i', 'verb you/sing'],
            ['-${isc}e', 'verb he/hse/it'],
            ['-iamo', 'verb we'],
            ['-ite', 'verb you/pl'],
            ['-${isc}ono', 'verb they'],

            ['-endo', 'gerund'],
            ['-endomi', 'gerund me'],
            ['-endolo', 'gerund him'],
            ['-endoli', 'gerund him/pl'],
            ['-endola', 'gerund her'],
            ['-endole', 'gerund her/pl '],
            ['-endosi', 'gerund -ing + him/her/themselves'],

            ['-ente', 'pres. part. -ing sing ??'],
            ['-endi', 'pres. part. -ing pl ??'],

            ['-endo', 'pres. part. -ing masc ??'],
            ['-ito', 'past part. -ing masc'],
            ['-enda', 'pres. part. -ing fem'],
            ['-ita', 'past part. -ing fem'],

            ['-ir&ograve', 'verb future I'],
            ['-irai', 'verb future you/sing'],
            ['-ir&agrave;', 'verb future s/he'],
            ['-iremo', 'verb future we'],
            ['-irete', 'verb future you/pl'],
            ['-iranno', 'verb future they'],
        ],
    }

    weird_rules = {
        '-e': [
            ['-e', 'verb infinite'],
            ['-', 'verb infinite'],
            ['-si', 'verb inf + reflexive he/they'],
            ['-lo', 'verb inf + masc sing'],
            ['-li', 'verb inf + masc pl'],
            ['-li', 'verb inf + fem sing'],
            ['-le', 'verb inf + fem pl'],
        ],
    }

    # verb post-rule: ducere$ -> durre
    # XXX get rid of me after examining the dictionary

