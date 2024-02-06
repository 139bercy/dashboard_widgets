import pandas as pd

def customIndex():
    customIndex = [
        "Fiche",
        "Juridiction",
        "codeNATINF",
        "codeNATINFconnexe",
        "infraction",
        "personne",
        "sexe",
        "anneeNaissance",
        "ageMomentFaits",
        "qualitePrevenus",
        "secteurPublic",
        "secteurPrive",
        "categorieSocioprofessionnelle",
        "descriptionModeOperatoire",
        "montantEnjeux",
        "departementCommissionFaits",
        "regionCommissionFaits",
        "DebutPrevention",
        "AnneeDebutPrevention",
        "finPeriodePrevention",
        "dureePeriodePrevention",
        "origineAffaire"
    ]
    return pd.Index(