########################################################################################
#
# This file produces questions on Latin morphology in an XML file compatible with
# Moodle, enabling the quick creation of practice quizzes for students.
#
# More regular nouns and verbs can be added to the below dictionaries to increase
# the number of questions generated.
#
# Author: Benjamin Niedzielski (bniedzie@ucla.edu)
# Last Modified: August 31, 2017
########################################################################################

#Enter dictionary entries here in the appropriate category.  No extra commas are allowed
firstDecl = ["agricola, agricolae, m. farmer", "aqua, aquae, f. water", "fēmina, fēminae, f. woman",
             "fortūna, fortūnae, f. fortune", "nauta, nautae, m. sailor", "puella, puellae, f. girl", "rosa, rosae, f. rose"
             "casa, casae, f. house", "lūna, lūnae, f. moon", "pecūnia, pecūniae, f. money"];
secondDeclM = ["vir, virī, m. man", "servus, servī, m. slave", "ager, agrī, m. field", "amīcus, amīcī, m. friend",
               "dominus, dominī, m. master", "puer, puerī, m. boy", "fīlius, fīliī, m. son"];
secondDeclN = ["bellum, bellī, n. war", "dōnum, dōnī, n. gift", "cōnsilium, cōnsiliī, n. plan"];
thirdDeclConsMF = ["pater, patris, m. father", "dux, ducis, m. leader", "māter, mātris, f. mother", "lībertās, lībertātis, f. freedom"];
thirdDeclConsN = ["caput, capitis, n. head", "corpus, corporis, n. body", "carmen, carminis, n. song"];
thirdDeclIMF = ["nox, noctis, f. night (i-stem)", "pars, partis, f. part (i-stem)", "cīvis, cīvis, m./f. citizen"];
thirdDeclIN = ["mare, maris, n. sea (i-stem)"];
fourthDeclMF = ["manus, manūs, f. hand", "cāsus, cāsūs, m. misfortune", "metus, metūs, m. dread", "passus, passūs, m. step"];
fourthDeclN = ["genū, genūs, n. knee"];
fifthDecl = ["rēs, reī, f. matter", "fidēs, fideī, f. faith", "spēs, speī, f. hope"];

firstConjTrans = ["amō, amāre, amāvī, amātus, to love", "iuvō, iuvāre, iūvī, iūtus, to please",
                  "laudō, laudāre, laudāvī, laudātus, to praise", "optō, optāre, optāvī, optātus, to desire",
                  "superō, superāre, superāvī, superātus, to overcome", "vocō, vocāre, vocāvī, vocātus, to call",
                  "aedificō, aedificāre, aedificāvī, aedificātus, to build"];
firstConjIntrans = ["labōrō, labōrāre, labōrāvī, labōrātus, to work"];
firstConjDep = ["arbitror, arbitrārī, arbitrātus sum, to judge", "cōnor, cōnārī, cōnātus sum, to try"];

secondConjTrans = ["dēbeō, dēbēre, dēbuī, dēbitus, to owe", "habeō, habēre, habuī, habitus, to owe",
                   "moneō, monēre, monuī, monitus, to warn", "terreō, terrēre, terruī, territus, to scare",
                   "videō, vidēre, vīdī, vīsus, to see", "impleō, implēre, implēvī, implētus, to fill"];
secondConjIntrans = ["taceō, tacēre, tacuī, tacitūrus, to be silent", "timeō, timēre, timuī, -, to fear"];
secondConjDep = ["vereor, verērī, veritus sum, to fear"];
secondConjSemiDep = ["audeō, audēre, ausus sum, to dare", "soleō, solēre, solitus sum, to be accustomed"];

thirdConjTrans = ["agō, agere, ēgī, actus, to perform", "dīcō, dīcere, dīxī, dictus, to say",
                  "dūcō, dūcere, dūxī, ductus, to lead", "legō, legere, lēgī, lēctus, to read",
                  "mittō, mittere, mīsī, missus, to send", "regō, regere, rēxī, rēctus, to rule",
                  "scrībō, scrībere, scrīpsī, scrīptus, to write"];
thirdConjIntrans = [];
thirdConjDep = ["loquor, loquī, locūtus sum, to say", "proficīscor, proficīscī, profectus sum, to set out"];
thirdConjSemiDep = ["fīdō, fīdere, fīsus sum, to trust"];

thirdIOConjTrans = ["capiō, capere, cēpī, captus, to take", "faciō, facere, fēcī, factus, to make",
                    "incipiō, incipere, incēpī, inceptus, to begin", "accipiō, accipere, accēpī, acceptus, to receive"];
thirdIOConjIntrans = ["fugiō, fugere, fūgī, fugitūrus, to flee"];
thirdIOConjDep = ["ingredior, ingredī, ingressus sum, to enter", "patior, patī, passus sum, to suffer"];

fourthConjTrans = ["audiō, audīre, audīvī, audītus, to hear", "sentiō, sentīre, sēnsī, sēnsus, to feel",
                   "fīniō, fīnīre, fīnīvī, fīnītus, to finish", "inveniō, invenīre, invēnī, inventus, to find"];
fourthConjIntrans = ["dormiō, dormīre, dormīvī, dormitūrus, to sleep", "veniō, venīre, vēnī, ventūrus, to come"];
fourthConjDep = ["potior, potīrī, potītus sum, to acquire"];

#The file will be created in the same folder as this program
outFile = 'testOut.xml';

#Contains the text to output as it is gradually built
outText = "";
#Used to ensure the output has proper indentation for human readability
indentLevel = 0;

#Add indents based on the current indent level, for making the XML file look nice
def addIndents():
    global outText;
    global indentLevel;
    for i in range(0, indentLevel):
        outText += "\t";

#Create the section of the XML file for the category name (corresponds to the path in the question bank, like a file path)
def createCategory(cat):
    global outText;
    global indentLevel;
    addIndents();
    outText += "<question type=\"category\">\n";
    indentLevel = indentLevel + 1;
    addIndents();
    outText += "<category>\n";
    indentLevel = indentLevel + 1;
    addIndents();
    outText += "<text>$course$/Default for latin_materials/" + cat + "</text>\n"
    indentLevel = indentLevel - 1;
    addIndents();
    outText += "</category>\n";
    indentLevel = indentLevel - 1;
    addIndents();
    outText += "</question>\n";
    return;

#Given word, recursively generates a list of all variations of word with and without proper macrons,
#changing only those starting from startChar.  Ensure the version with all correct macrons is first,
#since this is what Moodle shows as the correct answer after a quiz.
def getAnswers(word, startChar=0):
    #base case
    if (startChar == len(word)):
        return [word];
    #recursive case with macrons; split into 2 cases (with and without macron) and combine the lists
    if(word[startChar] == 'ā'):
        return getAnswers(word, startChar + 1) + getAnswers(word[0:startChar] + "a" + word[startChar+1:], startChar + 1);
    if(word[startChar] == 'ē'):
        return getAnswers(word, startChar + 1) + getAnswers(word[0:startChar] + "e" + word[startChar+1:], startChar + 1);
    if(word[startChar] == 'ī'):
        return getAnswers(word, startChar + 1) + getAnswers(word[0:startChar] + "i" + word[startChar+1:], startChar + 1);
    if(word[startChar] == 'ō'):
        return getAnswers(word, startChar + 1) + getAnswers(word[0:startChar] + "o" + word[startChar+1:], startChar + 1);
    if(word[startChar] == 'ū'):
        return getAnswers(word, startChar + 1) + getAnswers(word[0:startChar] + "u" + word[startChar+1:], startChar + 1);
    #recursive case with no macrons - check next letter for macrons
    return getAnswers(word, startChar + 1);

#Generates the XML code for a question, including the answers.  Feedback is currently not used, but would be specific feedback
#for each given answer (such as "remember the macron" for a 1st decl abl sing. answer of -a)
#Tracks indent level so the XML file looks fine when opened in a standard text editor
def createQuestion(name, text, answers, feedback):
    global outText;
    global indentLevel;
    addIndents();
    outText += "<question type=\"shortanswer\">\n";
    indentLevel = indentLevel + 1;
    addIndents();
    outText += "<name>\n";
    indentLevel = indentLevel + 1;
    addIndents();
    outText += ("<text>" + name + "</text>\n");
    indentLevel = indentLevel - 1;
    addIndents();
    outText += "</name>\n";
    addIndents();
    outText += "<questiontext format=\"html\">\n";
    indentLevel = indentLevel + 1;
    addIndents();
    outText += "<text>\n";
    indentLevel = indentLevel + 1;
    addIndents();
    outText += "<![CDATA[";
    outText += ("<p>" + text + "</p>");
    addIndents();
    outText += "]]>\n";    
    indentLevel = indentLevel - 1;
    addIndents();
    outText += "</text>\n"
    indentLevel = indentLevel - 1;    
    addIndents();
    outText += "</questiontext>\n";
    addIndents();
    outText += "<generalfeedback format=\"html\">\n";
    indentLevel = indentLevel + 1;
    addIndents();
    outText += "<text/>\n";
    indentLevel = indentLevel - 1;
    addIndents();
    outText += "</generalfeedback>\n";
    addIndents();
    outText += "<defaultgrade>1.0000000</defaultgrade>\n";
    addIndents();
    outText += "<penalty>0.3333333</penalty>\n";
    addIndents();
    outText += "<hidden>0</hidden>\n";
    addIndents();
    outText += "<usecase>0</usecase>\n";
    for ans in answers:
        addIndents();
        #Give answer full credit
        outText += "<answer format=\"moodle_auto_format\" fraction=\"100\">\n";
        indentLevel = indentLevel + 1;
        addIndents();
        outText += ("<text>" + ans + "</text>\n");
        addIndents();
        outText += "<feedback format=\"html\">\n";
        indentLevel = indentLevel + 1;
        addIndents();
        outText += "<text/>\n";
        indentLevel = indentLevel - 1;
        addIndents();
        outText += "</feedback>\n";
        indentLevel = indentLevel - 1;
        addIndents();
        outText += "</answer>\n";
    indentLevel = indentLevel - 1;
    addIndents();
    outText += "</question>\n";
    return;

#The below functions create questions for each type of morphology, by splitting up each relevant dictionary entry,
#getting the appropriate stem, and adding the appropriate endings.
#Some code is superfluous, and this can be done more elegantly, but this method is safe and works.
def createFirstDeclQuestions():
    global firstDecl;
    for entry in firstDecl:
        strippedEntry = [x.strip() for x in entry.split(',')]
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-2];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "ae"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(stem + "am"), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "ā"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "ae"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "ārum"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "īs"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "ās"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "īs"), []);

def createSecondDeclMQuestions():
    global secondDeclM;
    for entry in secondDeclM:
        strippedEntry = [x.strip() for x in entry.split(',')]
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-1];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "ō"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(stem + "um"), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "ō"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "ī"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "ōrum"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "īs"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "ōs"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "īs"), []);

def createSecondDeclNQuestions():
    global secondDeclN;
    for entry in secondDeclN:
        strippedEntry = [x.strip() for x in entry.split(',')]
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-1];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "ō"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(stem + "um"), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "ō"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "a"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "ōrum"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "īs"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "a"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "īs"), []);

def createThirdDeclConsMFQuestions():
    global thirdDeclConsMF;
    for entry in thirdDeclConsMF:
        strippedEntry = [x.strip() for x in entry.split(',')]
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-2];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "ī"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(stem + "em"), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "e"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "ēs"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "um"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "ibus"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "ēs"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "ibus"), []);

def createThirdDeclConsNQuestions():
    global thirdDeclConsN;
    for entry in thirdDeclConsN:
        strippedEntry = [x.strip() for x in entry.split(',')]
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-2];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "ī"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(nom), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "e"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "a"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "um"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "ibus"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "a"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "ibus"), []);

def createThirdDeclIMFQuestions():
    global thirdDeclIMF;
    for entry in thirdDeclIMF:
        strippedEntry = [x.strip() for x in entry.split(',')]
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-2];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "ī"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(stem + "em"), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "e"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "ēs"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "ium"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "ibus"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "ēs"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "ibus"), []);

def createThirdDeclINQuestions():
    global thirdDeclIN;
    for entry in thirdDeclIN:
        strippedEntry = [x.strip() for x in entry.split(',')]
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-2];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "ī"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(nom), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "e") + getAnswers(stem + "ī"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "ia"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "ium"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "ibus"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "ia"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "ibus"), []);

def createFourthDeclMFQuestions():
    global fourthDeclMF;
    for entry in fourthDeclMF:
        strippedEntry = [x.strip() for x in entry.split(',')]
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-2];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "uī"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(stem + "um"), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "ū"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "ūs"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "uum"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "ibus"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "ūs"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "ibus"), []);

def createFourthDeclNQuestions():
    global fourthDeclN;
    for entry in fourthDeclN:
        strippedEntry = [x.strip() for x in entry.split(',')]
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-2];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "ū"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(stem + "ū"), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "ū"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "ua"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "uum"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "ibus"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "ua"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "ibus"), []);

def createFifthDeclQuestions():
    global fifthDecl;
    for entry in fifthDecl:
        strippedEntry = [x.strip() for x in entry.split(',')];
        nom = strippedEntry[0];
        gen = strippedEntry[1];
        stem = gen[:-2];
        gender = (strippedEntry[2].split('.'))[0];
        meaning = ((strippedEntry[2].split('.'))[1]).split();
        #createQuestion("Nominative Singular of " + nom, "Produce the nominative singular of " + entry, getAnswers(nom), []);
        #createQuestion("Genitive Singular of " + nom, "Produce the genitive singular of " + entry, getAnswers(gen), []);
        createQuestion("Dative Singular of " + nom, "Produce the dative singular of " + entry, getAnswers(stem + "eī"), []);
        createQuestion("Accusative Singular of " + nom, "Produce the accusative singular of " + entry, getAnswers(stem + "em"), []);
        createQuestion("Ablative Singular of " + nom, "Produce the ablative singular of " + entry, getAnswers(stem + "ē"), []);
        createQuestion("Nominative Plural of " + nom, "Produce the nominative plural of " + entry, getAnswers(stem + "ēs"), []);
        createQuestion("Genitive Plural of " + nom, "Produce the genitive plural of " + entry, getAnswers(stem + "ērum"), []);
        createQuestion("Dative Plural of " + nom, "Produce the dative plural of " + entry, getAnswers(stem + "ēbus"), []);
        createQuestion("Accusative Plural of " + nom, "Produce the accusative plural of " + entry, getAnswers(stem + "ēs"), []);
        createQuestion("Ablative Plural of " + nom, "Produce the ablative plural of " + entry, getAnswers(stem + "ēbus"), []);

def createFirstConjPresActIndicQuestions():
    global firstConjTrans;
    global firstConjIntrans;
    for entry in (firstConjTrans + firstConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Present Active Indicative of " + firstPP, "Produce the 1st person singular present active indicative of " + entry, getAnswers(presStem + "ō"), []);
        createQuestion("Second Person Singular Present Active Indicative of " + firstPP, "Produce the 2nd person singular present active indicative of " + entry, getAnswers(presStem + "ās"), []);
        createQuestion("Third Person Singular Present Active Indicative of " + firstPP, "Produce the 3rd person singular present active indicative of " + entry, getAnswers(presStem + "at"), []);
        createQuestion("First Person Plural Present Active Indicative of " + firstPP, "Produce the 1st person plural present active indicative of " + entry, getAnswers(presStem + "āmus"), []);
        createQuestion("Second Person Plural Present Active Indicative of " + firstPP, "Produce the 2nd person plural present active indicative of " + entry, getAnswers(presStem + "ātis"), []);
        createQuestion("Third Person Plural Present Active Indicative of " + firstPP, "Produce the 3rd person plural present active indicative of " + entry, getAnswers(presStem + "ant"), []);

def createSecondConjPresActIndicQuestions():
    global secondConjTrans;
    global secondConjIntrans;
    for entry in (secondConjTrans + secondConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Present Active Indicative of " + firstPP, "Produce the 1st person singular present active indicative of " + entry, getAnswers(presStem + "eō"), []);
        createQuestion("Second Person Singular Present Active Indicative of " + firstPP, "Produce the 2nd person singular present active indicative of " + entry, getAnswers(presStem + "ēs"), []);
        createQuestion("Third Person Singular Present Active Indicative of " + firstPP, "Produce the 3rd person singular present active indicative of " + entry, getAnswers(presStem + "et"), []);
        createQuestion("First Person Plural Present Active Indicative of " + firstPP, "Produce the 1st person plural present active indicative of " + entry, getAnswers(presStem + "ēmus"), []);
        createQuestion("Second Person Plural Present Active Indicative of " + firstPP, "Produce the 2nd person plural present active indicative of " + entry, getAnswers(presStem + "ētis"), []);
        createQuestion("Third Person Plural Present Active Indicative of " + firstPP, "Produce the 3rd person plural present active indicative of " + entry, getAnswers(presStem + "ent"), []);

def createThirdConjPresActIndicQuestions():
    global thirdConjTrans;
    global thirdConjIntrans;
    for entry in (thirdConjTrans + thirdConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Present Active Indicative of " + firstPP, "Produce the 1st person singular present active indicative of " + entry, getAnswers(presStem + "ō"), []);
        createQuestion("Second Person Singular Present Active Indicative of " + firstPP, "Produce the 2nd person singular present active indicative of " + entry, getAnswers(presStem + "is"), []);
        createQuestion("Third Person Singular Present Active Indicative of " + firstPP, "Produce the 3rd person singular present active indicative of " + entry, getAnswers(presStem + "it"), []);
        createQuestion("First Person Plural Present Active Indicative of " + firstPP, "Produce the 1st person plural present active indicative of " + entry, getAnswers(presStem + "imus"), []);
        createQuestion("Second Person Plural Present Active Indicative of " + firstPP, "Produce the 2nd person plural present active indicative of " + entry, getAnswers(presStem + "itis"), []);
        createQuestion("Third Person Plural Present Active Indicative of " + firstPP, "Produce the 3rd person plural present active indicative of " + entry, getAnswers(presStem + "unt"), []);

def createThirdIOConjPresActIndicQuestions():
    global thirdIOConjTrans;
    global thirdIOConjIntrans;
    for entry in (thirdIOConjTrans + thirdIOConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Present Active Indicative of " + firstPP, "Produce the 1st person singular present active indicative of " + entry, getAnswers(presStem + "iō"), []);
        createQuestion("Second Person Singular Present Active Indicative of " + firstPP, "Produce the 2nd person singular present active indicative of " + entry, getAnswers(presStem + "is"), []);
        createQuestion("Third Person Singular Present Active Indicative of " + firstPP, "Produce the 3rd person singular present active indicative of " + entry, getAnswers(presStem + "it"), []);
        createQuestion("First Person Plural Present Active Indicative of " + firstPP, "Produce the 1st person plural present active indicative of " + entry, getAnswers(presStem + "imus"), []);
        createQuestion("Second Person Plural Present Active Indicative of " + firstPP, "Produce the 2nd person plural present active indicative of " + entry, getAnswers(presStem + "itis"), []);
        createQuestion("Third Person Plural Present Active Indicative of " + firstPP, "Produce the 3rd person plural present active indicative of " + entry, getAnswers(presStem + "iunt"), []);

def createFourthConjPresActIndicQuestions():
    global fourthConjTrans;
    global fourthConjIntrans;
    for entry in (fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Present Active Indicative of " + firstPP, "Produce the 1st person singular present active indicative of " + entry, getAnswers(presStem + "iō"), []);
        createQuestion("Second Person Singular Present Active Indicative of " + firstPP, "Produce the 2nd person singular present active indicative of " + entry, getAnswers(presStem + "īs"), []);
        createQuestion("Third Person Singular Present Active Indicative of " + firstPP, "Produce the 3rd person singular present active indicative of " + entry, getAnswers(presStem + "it"), []);
        createQuestion("First Person Plural Present Active Indicative of " + firstPP, "Produce the 1st person plural present active indicative of " + entry, getAnswers(presStem + "īmus"), []);
        createQuestion("Second Person Plural Present Active Indicative of " + firstPP, "Produce the 2nd person plural present active indicative of " + entry, getAnswers(presStem + "ītis"), []);
        createQuestion("Third Person Plural Present Active Indicative of " + firstPP, "Produce the 3rd person plural present active indicative of " + entry, getAnswers(presStem + "iunt"), []);

def createFirstConjImpfActIndicQuestions():
    global firstConjTrans;
    global firstConjIntrans;
    for entry in (firstConjTrans + firstConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 1st person singular imperfect active indicative of " + entry, getAnswers(presStem + "ābam"), []);
        createQuestion("Second Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 2nd person singular imperfect active indicative of " + entry, getAnswers(presStem + "ābās"), []);
        createQuestion("Third Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 3rd person singular imperfect active indicative of " + entry, getAnswers(presStem + "ābat"), []);
        createQuestion("First Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 1st person plural imperfect active indicative of " + entry, getAnswers(presStem + "ābāmus"), []);
        createQuestion("Second Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 2nd person plural imperfect active indicative of " + entry, getAnswers(presStem + "ābātis"), []);
        createQuestion("Third Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 3rd person plural imperfect active indicative of " + entry, getAnswers(presStem + "ābant"), []);

def createSecondConjImpfActIndicQuestions():
    global secondConjTrans;
    global secondConjIntrans;
    for entry in (secondConjTrans + secondConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 1st person singular imperfect active indicative of " + entry, getAnswers(presStem + "ēbam"), []);
        createQuestion("Second Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 2nd person singular imperfect active indicative of " + entry, getAnswers(presStem + "ēbās"), []);
        createQuestion("Third Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 3rd person singular imperfect active indicative of " + entry, getAnswers(presStem + "ēbat"), []);
        createQuestion("First Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 1st person plural imperfect active indicative of " + entry, getAnswers(presStem + "ēbāmus"), []);
        createQuestion("Second Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 2nd person plural imperfect active indicative of " + entry, getAnswers(presStem + "ēbātis"), []);
        createQuestion("Third Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 3rd person plural imperfect active indicative of " + entry, getAnswers(presStem + "ēbant"), []);

def createThirdConjImpfActIndicQuestions():
    global thirdConjTrans;
    global thirdConjIntrans;
    for entry in (thirdConjTrans + thirdConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 1st person singular imperfect active indicative of " + entry, getAnswers(presStem + "ēbam"), []);
        createQuestion("Second Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 2nd person singular imperfect active indicative of " + entry, getAnswers(presStem + "ēbās"), []);
        createQuestion("Third Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 3rd person singular imperfect active indicative of " + entry, getAnswers(presStem + "ēbat"), []);
        createQuestion("First Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 1st person plural imperfect active indicative of " + entry, getAnswers(presStem + "ēbāmus"), []);
        createQuestion("Second Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 2nd person plural imperfect active indicative of " + entry, getAnswers(presStem + "ēbātis"), []);
        createQuestion("Third Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 3rd person plural imperfect active indicative of " + entry, getAnswers(presStem + "ēbant"), []);

def createThirdIOConjImpfActIndicQuestions():
    global thirdIOConjTrans;
    global thirdIOConjIntrans;
    for entry in (thirdIOConjTrans + thirdIOConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 1st person singular imperfect active indicative of " + entry, getAnswers(presStem + "iēbam"), []);
        createQuestion("Second Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 2nd person singular imperfect active indicative of " + entry, getAnswers(presStem + "iēbās"), []);
        createQuestion("Third Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 3rd person singular imperfect active indicative of " + entry, getAnswers(presStem + "iēbat"), []);
        createQuestion("First Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 1st person plural imperfect active indicative of " + entry, getAnswers(presStem + "iēbāmus"), []);
        createQuestion("Second Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 2nd person plural imperfect active indicative of " + entry, getAnswers(presStem + "iēbātis"), []);
        createQuestion("Third Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 3rd person plural imperfect active indicative of " + entry, getAnswers(presStem + "iēbant"), []);

def createFourthConjImpfActIndicQuestions():
    global fourthConjTrans;
    global fourthConjIntrans;
    for entry in (fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 1st person singular imperfect active indicative of " + entry, getAnswers(presStem + "iēbam"), []);
        createQuestion("Second Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 2nd person singular imperfect active indicative of " + entry, getAnswers(presStem + "iēbās"), []);
        createQuestion("Third Person Singular Imperfect Active Indicative of " + firstPP, "Produce the 3rd person singular imperfect active indicative of " + entry, getAnswers(presStem + "iēbat"), []);
        createQuestion("First Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 1st person plural imperfect active indicative of " + entry, getAnswers(presStem + "iēbāmus"), []);
        createQuestion("Second Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 2nd person plural imperfect active indicative of " + entry, getAnswers(presStem + "iēbātis"), []);
        createQuestion("Third Person Plural Imperfect Active Indicative of " + firstPP, "Produce the 3rd person plural imperfect active indicative of " + entry, getAnswers(presStem + "iēbant"), []);

def createFirstConjFutActIndicQuestions():
    global firstConjTrans;
    global firstConjIntrans;
    for entry in (firstConjTrans + firstConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Active Indicative of " + firstPP, "Produce the 1st person singular future active indicative of " + entry, getAnswers(presStem + "ābō"), []);
        createQuestion("Second Person Singular Future Active Indicative of " + firstPP, "Produce the 2nd person singular future active indicative of " + entry, getAnswers(presStem + "ābis"), []);
        createQuestion("Third Person Singular Future Active Indicative of " + firstPP, "Produce the 3rd person singular future active indicative of " + entry, getAnswers(presStem + "ābit"), []);
        createQuestion("First Person Plural Future Active Indicative of " + firstPP, "Produce the 1st person plural future active indicative of " + entry, getAnswers(presStem + "ābimus"), []);
        createQuestion("Second Person Plural Future Active Indicative of " + firstPP, "Produce the 2nd person plural future active indicative of " + entry, getAnswers(presStem + "ābitis"), []);
        createQuestion("Third Person Plural Future Active Indicative of " + firstPP, "Produce the 3rd person plural future active indicative of " + entry, getAnswers(presStem + "ābunt"), []);

def createSecondConjFutActIndicQuestions():
    global secondConjTrans;
    global secondConjIntrans;
    for entry in (secondConjTrans + secondConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Active Indicative of " + firstPP, "Produce the 1st person singular future active indicative of " + entry, getAnswers(presStem + "ēbō"), []);
        createQuestion("Second Person Singular Future Active Indicative of " + firstPP, "Produce the 2nd person singular future active indicative of " + entry, getAnswers(presStem + "ēbis"), []);
        createQuestion("Third Person Singular Future Active Indicative of " + firstPP, "Produce the 3rd person singular future active indicative of " + entry, getAnswers(presStem + "ēbit"), []);
        createQuestion("First Person Plural Future Active Indicative of " + firstPP, "Produce the 1st person plural future active indicative of " + entry, getAnswers(presStem + "ēbimus"), []);
        createQuestion("Second Person Plural Future Active Indicative of " + firstPP, "Produce the 2nd person plural future active indicative of " + entry, getAnswers(presStem + "ēbitis"), []);
        createQuestion("Third Person Plural Future Active Indicative of " + firstPP, "Produce the 3rd person plural future active indicative of " + entry, getAnswers(presStem + "ēbunt"), []);

def createThirdConjFutActIndicQuestions():
    global thirdConjTrans;
    global thirdConjIntrans;
    for entry in (thirdConjTrans + thirdConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Active Indicative of " + firstPP, "Produce the 1st person singular future active indicative of " + entry, getAnswers(presStem + "am"), []);
        createQuestion("Second Person Singular Future Active Indicative of " + firstPP, "Produce the 2nd person singular future active indicative of " + entry, getAnswers(presStem + "ēs"), []);
        createQuestion("Third Person Singular Future Active Indicative of " + firstPP, "Produce the 3rd person singular future active indicative of " + entry, getAnswers(presStem + "et"), []);
        createQuestion("First Person Plural Future Active Indicative of " + firstPP, "Produce the 1st person plural future active indicative of " + entry, getAnswers(presStem + "ēmus"), []);
        createQuestion("Second Person Plural Future Active Indicative of " + firstPP, "Produce the 2nd person plural future active indicative of " + entry, getAnswers(presStem + "ētis"), []);
        createQuestion("Third Person Plural Future Active Indicative of " + firstPP, "Produce the 3rd person plural future active indicative of " + entry, getAnswers(presStem + "ent"), []);
        
def createThirdIOConjFutActIndicQuestions():
    global thirdIOConjTrans;
    global thirdIOConjIntrans;
    for entry in (thirdIOConjTrans + thirdIOConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Active Indicative of " + firstPP, "Produce the 1st person singular future active indicative of " + entry, getAnswers(presStem + "iam"), []);
        createQuestion("Second Person Singular Future Active Indicative of " + firstPP, "Produce the 2nd person singular future active indicative of " + entry, getAnswers(presStem + "iēs"), []);
        createQuestion("Third Person Singular Future Active Indicative of " + firstPP, "Produce the 3rd person singular future active indicative of " + entry, getAnswers(presStem + "iet"), []);
        createQuestion("First Person Plural Future Active Indicative of " + firstPP, "Produce the 1st person plural future active indicative of " + entry, getAnswers(presStem + "iēmus"), []);
        createQuestion("Second Person Plural Future Active Indicative of " + firstPP, "Produce the 2nd person plural future active indicative of " + entry, getAnswers(presStem + "iētis"), []);
        createQuestion("Third Person Plural Future Active Indicative of " + firstPP, "Produce the 3rd person plural future active indicative of " + entry, getAnswers(presStem + "ient"), []);

def createFourthConjFutActIndicQuestions():
    global fourthConjTrans;
    global fourthConjIntrans;
    for entry in (fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Active Indicative of " + firstPP, "Produce the 1st person singular future active indicative of " + entry, getAnswers(presStem + "iam"), []);
        createQuestion("Second Person Singular Future Active Indicative of " + firstPP, "Produce the 2nd person singular future active indicative of " + entry, getAnswers(presStem + "iēs"), []);
        createQuestion("Third Person Singular Future Active Indicative of " + firstPP, "Produce the 3rd person singular future active indicative of " + entry, getAnswers(presStem + "iet"), []);
        createQuestion("First Person Plural Future Active Indicative of " + firstPP, "Produce the 1st person plural future active indicative of " + entry, getAnswers(presStem + "iēmus"), []);
        createQuestion("Second Person Plural Future Active Indicative of " + firstPP, "Produce the 2nd person plural future active indicative of " + entry, getAnswers(presStem + "iētis"), []);
        createQuestion("Third Person Plural Future Active Indicative of " + firstPP, "Produce the 3rd person plural future active indicative of " + entry, getAnswers(presStem + "ient"), []);

def createFirstConjPresPassIndicQuestions():
    global firstConjTrans;
    for entry in (firstConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Present Passive Indicative of " + firstPP, "Produce the 1st person singular present passive indicative of " + entry, getAnswers(presStem + "or"), []);
        createQuestion("Second Person Singular Present Passive Indicative of " + firstPP, "Produce the 2nd person singular present passive indicative of " + entry, getAnswers(presStem + "āris") + getAnswers(presStem + "āre"), []);
        createQuestion("Third Person Singular Present Passive Indicative of " + firstPP, "Produce the 3rd person singular present passive indicative of " + entry, getAnswers(presStem + "ātur"), []);
        createQuestion("First Person Plural Present Passive Indicative of " + firstPP, "Produce the 1st person plural present passive indicative of " + entry, getAnswers(presStem + "āmur"), []);
        createQuestion("Second Person Plural Present Passive Indicative of " + firstPP, "Produce the 2nd person plural present passive indicative of " + entry, getAnswers(presStem + "āminī"), []);
        createQuestion("Third Person Plural Present Passive Indicative of " + firstPP, "Produce the 3rd person plural present passive indicative of " + entry, getAnswers(presStem + "antur"), []);

def createSecondConjPresPassIndicQuestions():
    global secondConjTrans;
    for entry in (secondConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Present Passive Indicative of " + firstPP, "Produce the 1st person singular present passive indicative of " + entry, getAnswers(presStem + "eor"), []);
        createQuestion("Second Person Singular Present Passive Indicative of " + firstPP, "Produce the 2nd person singular present passive indicative of " + entry, getAnswers(presStem + "ēris") + getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Present Passive Indicative of " + firstPP, "Produce the 3rd person singular present passive indicative of " + entry, getAnswers(presStem + "ētur"), []);
        createQuestion("First Person Plural Present Passive Indicative of " + firstPP, "Produce the 1st person plural present passive indicative of " + entry, getAnswers(presStem + "ēmur"), []);
        createQuestion("Second Person Plural Present Passive Indicative of " + firstPP, "Produce the 2nd person plural present passive indicative of " + entry, getAnswers(presStem + "ēminī"), []);
        createQuestion("Third Person Plural Present Passive Indicative of " + firstPP, "Produce the 3rd person plural present passive indicative of " + entry, getAnswers(presStem + "entur"), []);

def createThirdConjPresPassIndicQuestions():
    global thirdConjTrans;
    for entry in (thirdConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Present Passive Indicative of " + firstPP, "Produce the 1st person singular present passive indicative of " + entry, getAnswers(presStem + "or"), []);
        createQuestion("Second Person Singular Present Passive Indicative of " + firstPP, "Produce the 2nd person singular present passive indicative of " + entry, getAnswers(presStem + "eris") + getAnswers(presStem + "ere"), []);
        createQuestion("Third Person Singular Present Passive Indicative of " + firstPP, "Produce the 3rd person singular present passive indicative of " + entry, getAnswers(presStem + "itur"), []);
        createQuestion("First Person Plural Present Passive Indicative of " + firstPP, "Produce the 1st person plural present passive indicative of " + entry, getAnswers(presStem + "imur"), []);
        createQuestion("Second Person Plural Present Passive Indicative of " + firstPP, "Produce the 2nd person plural present passive indicative of " + entry, getAnswers(presStem + "iminī"), []);
        createQuestion("Third Person Plural Present Passive Indicative of " + firstPP, "Produce the 3rd person plural present passive indicative of " + entry, getAnswers(presStem + "untur"), []);

def createThirdIOConjPresPassIndicQuestions():
    global thirdIOConjTrans;
    for entry in (thirdIOConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        if firstPP != "faciō":
            createQuestion("First Person Singular Present Passive Indicative of " + firstPP, "Produce the 1st person singular present passive indicative of " + entry, getAnswers(presStem + "ior"), []);
            createQuestion("Second Person Singular Present Passive Indicative of " + firstPP, "Produce the 2nd person singular present passive indicative of " + entry, getAnswers(presStem + "eris") + getAnswers(presStem + "ere"), []);
            createQuestion("Third Person Singular Present Passive Indicative of " + firstPP, "Produce the 3rd person singular present passive indicative of " + entry, getAnswers(presStem + "itur"), []);
            createQuestion("First Person Plural Present Passive Indicative of " + firstPP, "Produce the 1st person plural present passive indicative of " + entry, getAnswers(presStem + "imur"), []);
            createQuestion("Second Person Plural Present Passive Indicative of " + firstPP, "Produce the 2nd person plural present passive indicative of " + entry, getAnswers(presStem + "iminī"), []);
            createQuestion("Third Person Plural Present Passive Indicative of " + firstPP, "Produce the 3rd person plural present passive indicative of " + entry, getAnswers(presStem + "iuntur"), []);

def createFourthConjPresPassIndicQuestions():
    global fourthConjTrans;
    for entry in (fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Present Passive Indicative of " + firstPP, "Produce the 1st person singular present passive indicative of " + entry, getAnswers(presStem + "ior"), []);
        createQuestion("Second Person Singular Present Passive Indicative of " + firstPP, "Produce the 2nd person singular present passive indicative of " + entry, getAnswers(presStem + "īris") + getAnswers(presStem + "īre"), []);
        createQuestion("Third Person Singular Present Passive Indicative of " + firstPP, "Produce the 3rd person singular present passive indicative of " + entry, getAnswers(presStem + "ītur"), []);
        createQuestion("First Person Plural Present Passive Indicative of " + firstPP, "Produce the 1st person plural present passive indicative of " + entry, getAnswers(presStem + "īmur"), []);
        createQuestion("Second Person Plural Present Passive Indicative of " + firstPP, "Produce the 2nd person plural present passive indicative of " + entry, getAnswers(presStem + "īminī"), []);
        createQuestion("Third Person Plural Present Passive Indicative of " + firstPP, "Produce the 3rd person plural present passive indicative of " + entry, getAnswers(presStem + "iuntur"), []);

def createFirstConjImpfPassIndicQuestions():
    global firstConjTrans;
    for entry in (firstConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 1st person singular imperfect passive indicative of " + entry, getAnswers(presStem + "ābar"), []);
        createQuestion("Second Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "ābāris")+getAnswers(presStem + "ābāre"), []);
        createQuestion("Third Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "ābātur"), []);
        createQuestion("First Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 1st person plural imperfect passive indicative of " + entry, getAnswers(presStem + "ābāmur"), []);
        createQuestion("Second Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "ābāminī"), []);
        createQuestion("Third Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "ābantur"), []);

def createSecondConjImpfPassIndicQuestions():
    global secondConjTrans;
    for entry in (secondConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 1st person singular imperfect passive indicative of " + entry, getAnswers(presStem + "ēbar"), []);
        createQuestion("Second Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "ēbāris")+getAnswers(presStem + "ēbāre"), []);
        createQuestion("Third Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "ēbātur"), []);
        createQuestion("First Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 1st person plural imperfect passive indicative of " + entry, getAnswers(presStem + "ēbāmur"), []);
        createQuestion("Second Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "ēbāminī"), []);
        createQuestion("Third Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "ēbantur"), []);

def createThirdConjImpfPassIndicQuestions():
    global thirdConjTrans;
    for entry in (thirdConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 1st person singular imperfect passive indicative of " + entry, getAnswers(presStem + "ēbar"), []);
        createQuestion("Second Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "ēbāris")+getAnswers(presStem + "ēbāre"), []);
        createQuestion("Third Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "ēbātur"), []);
        createQuestion("First Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 1st person plural imperfect passive indicative of " + entry, getAnswers(presStem + "ēbāmur"), []);
        createQuestion("Second Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "ēbāminī"), []);
        createQuestion("Third Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "ēbantur"), []);

def createThirdIOConjImpfPassIndicQuestions():
    global thirdIOConjTrans;
    for entry in (thirdIOConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        if firstPP != "faciō":
            createQuestion("First Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 1st person singular imperfect passive indicative of " + entry, getAnswers(presStem + "iēbar"), []);
            createQuestion("Second Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "iēbāris")+getAnswers(presStem + "iēbāre"), []);
            createQuestion("Third Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "iēbātur"), []);
            createQuestion("First Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 1st person plural imperfect passive indicative of " + entry, getAnswers(presStem + "iēbāmur"), []);
            createQuestion("Second Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "iēbāminī"), []);
            createQuestion("Third Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "iēbantur"), []);

def createFourthConjImpfPassIndicQuestions():
    global fourthConjTrans;
    for entry in (fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 1st person singular imperfect passive indicative of " + entry, getAnswers(presStem + "iēbar"), []);
        createQuestion("Second Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "iēbāris")+getAnswers(presStem + "iēbāre"), []);
        createQuestion("Third Person Singular Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person singular imperfect passive indicative of " + entry, getAnswers(presStem + "iēbātur"), []);
        createQuestion("First Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 1st person plural imperfect passive indicative of " + entry, getAnswers(presStem + "iēbāmur"), []);
        createQuestion("Second Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 2nd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "iēbāminī"), []);
        createQuestion("Third Person Plural Imperfect Passive Indicative of " + firstPP, "Produce the 3rd person plural imperfect passive indicative of " + entry, getAnswers(presStem + "iēbantur"), []);

def createFirstConjFutPassIndicQuestions():
    global firstConjTrans;
    for entry in (firstConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Passive Indicative of " + firstPP, "Produce the 1st person singular future passive indicative of " + entry, getAnswers(presStem + "ābor"), []);
        createQuestion("Second Person Singular Future Passive Indicative of " + firstPP, "Produce the 2nd person singular future passive indicative of " + entry, getAnswers(presStem + "āberis")+getAnswers(presStem + "ābere"), []);
        createQuestion("Third Person Singular Future Passive Indicative of " + firstPP, "Produce the 3rd person singular future passive indicative of " + entry, getAnswers(presStem + "ābitur"), []);
        createQuestion("First Person Plural Future Passive Indicative of " + firstPP, "Produce the 1st person plural future passive indicative of " + entry, getAnswers(presStem + "ābimur"), []);
        createQuestion("Second Person Plural Future Passive Indicative of " + firstPP, "Produce the 2nd person plural future passive indicative of " + entry, getAnswers(presStem + "ābiminī"), []);
        createQuestion("Third Person Plural Future Passive Indicative of " + firstPP, "Produce the 3rd person plural future passive indicative of " + entry, getAnswers(presStem + "ābuntur"), []);

def createSecondConjFutPassIndicQuestions():
    global secondConjTrans;
    for entry in (secondConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Passive Indicative of " + firstPP, "Produce the 1st person singular future passive indicative of " + entry, getAnswers(presStem + "ēbor"), []);
        createQuestion("Second Person Singular Future Passive Indicative of " + firstPP, "Produce the 2nd person singular future passive indicative of " + entry, getAnswers(presStem + "ēberis")+getAnswers(presStem + "ēbere"), []);
        createQuestion("Third Person Singular Future Passive Indicative of " + firstPP, "Produce the 3rd person singular future passive indicative of " + entry, getAnswers(presStem + "ēbitur"), []);
        createQuestion("First Person Plural Future Passive Indicative of " + firstPP, "Produce the 1st person plural future passive indicative of " + entry, getAnswers(presStem + "ēbimur"), []);
        createQuestion("Second Person Plural Future Passive Indicative of " + firstPP, "Produce the 2nd person plural future passive indicative of " + entry, getAnswers(presStem + "ēbiminī"), []);
        createQuestion("Third Person Plural Future Passive Indicative of " + firstPP, "Produce the 3rd person plural future passive indicative of " + entry, getAnswers(presStem + "ēbuntur"), []);

def createThirdConjFutPassIndicQuestions():
    global thirdConjTrans;
    for entry in (thirdConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Passive Indicative of " + firstPP, "Produce the 1st person singular future passive indicative of " + entry, getAnswers(presStem + "ar"), []);
        createQuestion("Second Person Singular Future Passive Indicative of " + firstPP, "Produce the 2nd person singular future passive indicative of " + entry, getAnswers(presStem + "ēris")+getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Future Passive Indicative of " + firstPP, "Produce the 3rd person singular future passive indicative of " + entry, getAnswers(presStem + "ētur"), []);
        createQuestion("First Person Plural Future Passive Indicative of " + firstPP, "Produce the 1st person plural future passive indicative of " + entry, getAnswers(presStem + "ēmur"), []);
        createQuestion("Second Person Plural Future Passive Indicative of " + firstPP, "Produce the 2nd person plural future passive indicative of " + entry, getAnswers(presStem + "ēminī"), []);
        createQuestion("Third Person Plural Future Passive Indicative of " + firstPP, "Produce the 3rd person plural future passive indicative of " + entry, getAnswers(presStem + "entur"), []);
        
def createThirdIOConjFutPassIndicQuestions():
    global thirdIOConjTrans;
    for entry in (thirdIOConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        if firstPP != "faciō":
            createQuestion("First Person Singular Future Passive Indicative of " + firstPP, "Produce the 1st person singular future passive indicative of " + entry, getAnswers(presStem + "iar"), []);
            createQuestion("Second Person Singular Future Passive Indicative of " + firstPP, "Produce the 2nd person singular future passive indicative of " + entry, getAnswers(presStem + "iēris")+getAnswers(presStem + "iēre"), []);
            createQuestion("Third Person Singular Future Passive Indicative of " + firstPP, "Produce the 3rd person singular future passive indicative of " + entry, getAnswers(presStem + "iētur"), []);
            createQuestion("First Person Plural Future Passive Indicative of " + firstPP, "Produce the 1st person plural future passive indicative of " + entry, getAnswers(presStem + "iēmur"), []);
            createQuestion("Second Person Plural Future Passive Indicative of " + firstPP, "Produce the 2nd person plural future passive indicative of " + entry, getAnswers(presStem + "iēminī"), []);
            createQuestion("Third Person Plural Future Passive Indicative of " + firstPP, "Produce the 3rd person plural future passive indicative of " + entry, getAnswers(presStem + "ientur"), []);

def createFourthConjFutPassIndicQuestions():
    global fourthConjTrans;
    for entry in (fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Passive Indicative of " + firstPP, "Produce the 1st person singular future passive indicative of " + entry, getAnswers(presStem + "iar"), []);
        createQuestion("Second Person Singular Future Passive Indicative of " + firstPP, "Produce the 2nd person singular future passive indicative of " + entry, getAnswers(presStem + "iēris")+getAnswers(presStem + "iēre"), []);
        createQuestion("Third Person Singular Future Passive Indicative of " + firstPP, "Produce the 3rd person singular future passive indicative of " + entry, getAnswers(presStem + "iētur"), []);
        createQuestion("First Person Plural Future Passive Indicative of " + firstPP, "Produce the 1st person plural future passive indicative of " + entry, getAnswers(presStem + "iēmur"), []);
        createQuestion("Second Person Plural Future Passive Indicative of " + firstPP, "Produce the 2nd person plural future passive indicative of " + entry, getAnswers(presStem + "iēminī"), []);
        createQuestion("Third Person Plural Future Passive Indicative of " + firstPP, "Produce the 3rd person plural future passive indicative of " + entry, getAnswers(presStem + "ientur"), []);

def createPerfActIndicQuestions():
    global firstConjTrans;
    global firstConjIntrans;
    global secondConjTrans;
    global secondConjIntrans;
    global thirdConjTrans;
    global thirdConjIntrans;
    global thirdIOConjTrans;
    global thirdIOConjIntrans;
    global fourthConjTrans;
    global fourthConjIntrans;
    
    for entry in (firstConjTrans + firstConjIntrans + secondConjTrans + secondConjIntrans + thirdConjTrans + thirdConjIntrans + thirdIOConjTrans + thirdIOConjIntrans + fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        strippedPerfStems = [(x.strip())[:-1] for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Perfect Active Indicative of " + firstPP, "Produce the 1st person singular perfect active indicative of " + entry, [getAnswers(x + "ī") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Singular Perfect Active Indicative of " + firstPP, "Produce the 2nd person singular perfect active indicative of " + entry, [getAnswers(x + "istī") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Singular Perfect Active Indicative of " + firstPP, "Produce the 3rd person singular perfect active indicative of " + entry, [getAnswers(x + "it") for x in strippedPerfStems][0], []);
        createQuestion("First Person Plural Perfect Active Indicative of " + firstPP, "Produce the 1st person plural perfect active indicative of " + entry, [getAnswers(x + "imus") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Plural Perfect Active Indicative of " + firstPP, "Produce the 2nd person plural perfect active indicative of " + entry, [getAnswers(x + "istis") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Plural Perfect Active Indicative of " + firstPP, "Produce the 3rd person plural perfect active indicative of " + entry, [getAnswers(x + "ērunt") for x in strippedPerfStems][0] + [getAnswers(x + "ēre") for x in strippedPerfStems][0], []);

def createPlpfActIndicQuestions():
    global firstConjTrans;
    global firstConjIntrans;
    global secondConjTrans;
    global secondConjIntrans;
    global thirdConjTrans;
    global thirdConjIntrans;
    global thirdIOConjTrans;
    global thirdIOConjIntrans;
    global fourthConjTrans;
    global fourthConjIntrans;
    
    for entry in (firstConjTrans + firstConjIntrans + secondConjTrans + secondConjIntrans + thirdConjTrans + thirdConjIntrans + thirdIOConjTrans + thirdIOConjIntrans + fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        strippedPerfStems = [(x.strip())[:-1] for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Pluperfect Active Indicative of " + firstPP, "Produce the 1st person singular pluperfect active indicative of " + entry, [getAnswers(x + "eram") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Singular Pluperfect Active Indicative of " + firstPP, "Produce the 2nd person singular pluperfect active indicative of " + entry, [getAnswers(x + "erās") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Singular Pluperfect Active Indicative of " + firstPP, "Produce the 3rd person singular pluperfect active indicative of " + entry, [getAnswers(x + "erat") for x in strippedPerfStems][0], []);
        createQuestion("First Person Plural Pluperfect Active Indicative of " + firstPP, "Produce the 1st person plural pluperfect active indicative of " + entry, [getAnswers(x + "erāmus") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Plural Pluperfect Active Indicative of " + firstPP, "Produce the 2nd person plural pluperfect active indicative of " + entry, [getAnswers(x + "erātis") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Plural Pluperfect Active Indicative of " + firstPP, "Produce the 3rd person plural pluperfect active indicative of " + entry, [getAnswers(x + "erant") for x in strippedPerfStems][0], []);

def createFPerfActIndicQuestions():
    global firstConjTrans;
    global firstConjIntrans;
    global secondConjTrans;
    global secondConjIntrans;
    global thirdConjTrans;
    global thirdConjIntrans;
    global thirdIOConjTrans;
    global thirdIOConjIntrans;
    global fourthConjTrans;
    global fourthConjIntrans;
    
    for entry in (firstConjTrans + firstConjIntrans + secondConjTrans + secondConjIntrans + thirdConjTrans + thirdConjIntrans + thirdIOConjTrans + thirdIOConjIntrans + fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        strippedPerfStems = [(x.strip())[:-1] for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Future Perfect Active Indicative of " + firstPP, "Produce the 1st person singular future perfect active indicative of " + entry, [getAnswers(x + "erō") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Singular Future Perfect Active Indicative of " + firstPP, "Produce the 2nd person singular future perfect active indicative of " + entry, [getAnswers(x + "eris") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Singular Future Perfect Active Indicative of " + firstPP, "Produce the 3rd person singular future perfect active indicative of " + entry, [getAnswers(x + "erit") for x in strippedPerfStems][0], []);
        createQuestion("First Person Plural Future Perfect Active Indicative of " + firstPP, "Produce the 1st person plural future perfect active indicative of " + entry, [getAnswers(x + "erimus") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Plural Future Perfect Active Indicative of " + firstPP, "Produce the 2nd person plural future perfect active indicative of " + entry, [getAnswers(x + "eritis") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Plural Future Perfect Active Indicative of " + firstPP, "Produce the 3rd person plural future perfect active indicative of " + entry, [getAnswers(x + "erint") for x in strippedPerfStems][0], []);

def createPerfPassIndicQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    
    for entry in (firstConjTrans + secondConjTrans + thirdConjTrans + thirdIOConjTrans + fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        stem = fourthPP[:-2];
        createQuestion("First Person Singular Perfect Passive Indicative of " + firstPP, "Produce the 1st person singular perfect passive indicative of " + entry, getAnswers(stem + "us sum") + getAnswers(stem + "a sum") + getAnswers(stem + "um sum"), []);
        createQuestion("Second Person Singular Perfect Passive Indicative of " + firstPP, "Produce the 2nd person singular perfect passive indicative of " + entry, getAnswers(stem + "us es") + getAnswers(stem + "a es") + getAnswers(stem + "um es"), []);
        createQuestion("Third Person Singular Perfect Passive Indicative of " + firstPP, "Produce the 3rd person singular perfect passive indicative of " + entry, getAnswers(stem + "us est") + getAnswers(stem + "a est") + getAnswers(stem + "um est"), []);
        createQuestion("First Person Plural Perfect Passive Indicative of " + firstPP, "Produce the 1st person plural perfect passive indicative of " + entry, getAnswers(stem + "ī sumus") + getAnswers(stem + "ae sumus") + getAnswers(stem + "a sumus"), []);
        createQuestion("Second Person Plural Perfect Passive Indicative of " + firstPP, "Produce the 2nd person plural perfect passive indicative of " + entry, getAnswers(stem + "ī estis") + getAnswers(stem + "ae estis") + getAnswers(stem + "a estis"), []);
        createQuestion("Third Person Plural Perfect Passive Indicative of " + firstPP, "Produce the 3rd person plural perfect passive indicative of " + entry, getAnswers(stem + "ī sunt") + getAnswers(stem + "ae sunt") + getAnswers(stem + "a sunt"), []);

def createPlpfPassIndicQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    
    for entry in (firstConjTrans + secondConjTrans + thirdConjTrans + thirdIOConjTrans + fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        stem = fourthPP[:-2];
        createQuestion("First Person Singular Pluperfect Passive Indicative of " + firstPP, "Produce the 1st person singular pluperfect passive indicative of " + entry, getAnswers(stem + "us eram") + getAnswers(stem + "a eram") + getAnswers(stem + "um eram"), []);
        createQuestion("Second Person Singular Pluperfect Passive Indicative of " + firstPP, "Produce the 2nd person singular pluperfect passive indicative of " + entry, getAnswers(stem + "us erās") + getAnswers(stem + "a erās") + getAnswers(stem + "um erās"), []);
        createQuestion("Third Person Singular Pluperfect Passive Indicative of " + firstPP, "Produce the 3rd person singular pluperfect passive indicative of " + entry, getAnswers(stem + "us erat") + getAnswers(stem + "a erat") + getAnswers(stem + "um erat"), []);
        createQuestion("First Person Plural Pluperfect Passive Indicative of " + firstPP, "Produce the 1st person plural pluperfect passive indicative of " + entry, getAnswers(stem + "ī erāmus") + getAnswers(stem + "ae erāmus") + getAnswers(stem + "a erāmus"), []);
        createQuestion("Second Person Plural Pluperfect Passive Indicative of " + firstPP, "Produce the 2nd person plural pluperfect passive indicative of " + entry, getAnswers(stem + "ī erātis") + getAnswers(stem + "ae erātis") + getAnswers(stem + "a erātis"), []);
        createQuestion("Third Person Plural Pluperfect Passive Indicative of " + firstPP, "Produce the 3rd person plural pluperfect passive indicative of " + entry, getAnswers(stem + "ī erant") + getAnswers(stem + "ae erant") + getAnswers(stem + "a erant"), []);

def createFPerfPassIndicQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    
    for entry in (firstConjTrans + secondConjTrans + thirdConjTrans + thirdIOConjTrans + fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        stem = fourthPP[:-2];
        createQuestion("First Person Singular Future Perfect Passive Indicative of " + firstPP, "Produce the 1st person singular future perfect passive indicative of " + entry, getAnswers(stem + "us erō") + getAnswers(stem + "a erō") + getAnswers(stem + "um erō"), []);
        createQuestion("Second Person Singular Future Perfect Passive Indicative of " + firstPP, "Produce the 2nd person singular future perfect passive indicative of " + entry, getAnswers(stem + "us eris") + getAnswers(stem + "a eris") + getAnswers(stem + "um eris"), []);
        createQuestion("Third Person Singular Future Perfect Passive Indicative of " + firstPP, "Produce the 3rd person singular future perfect passive indicative of " + entry, getAnswers(stem + "us erit") + getAnswers(stem + "a erit") + getAnswers(stem + "um erit"), []);
        createQuestion("First Person Plural Future Perfect Passive Indicative of " + firstPP, "Produce the 1st person plural future perfect passive indicative of " + entry, getAnswers(stem + "ī erimus") + getAnswers(stem + "ae erimus") + getAnswers(stem + "a erimus"), []);
        createQuestion("Second Person Plural Future Perfect Passive Indicative of " + firstPP, "Produce the 2nd person plural future perfect passive indicative of " + entry, getAnswers(stem + "ī eritis") + getAnswers(stem + "ae eritis") + getAnswers(stem + "a eritis"), []);
        createQuestion("Third Person Plural Future Perfect Passive Indicative of " + firstPP, "Produce the 3rd person plural future perfect passive indicative of " + entry, getAnswers(stem + "ī erunt") + getAnswers(stem + "ae erunt") + getAnswers(stem + "a erunt"), []);

def createDeponentIndicQuestions():
    global firstConjDep;
    global secondConjDep;
    global thirdConjDep;
    global thirdIOConjDep;
    global fourthConjDep;

    for entry in (firstConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Deponent Indicative of " + firstPP, "Produce the 1st person singular present deponent indicative of " + entry, getAnswers(presStem + "or"), []);
        createQuestion("Second Person Singular Present Deponent Indicative of " + firstPP, "Produce the 2nd person singular present deponent indicative of " + entry, getAnswers(presStem + "āris") + getAnswers(presStem + "āre"), []);
        createQuestion("Third Person Singular Present Deponent Indicative of " + firstPP, "Produce the 3rd person singular present deponent indicative of " + entry, getAnswers(presStem + "ātur"), []);
        createQuestion("First Person Plural Present Deponent Indicative of " + firstPP, "Produce the 1st person plural present deponent indicative of " + entry, getAnswers(presStem + "āmur"), []);
        createQuestion("Second Person Plural Present Deponent Indicative of " + firstPP, "Produce the 2nd person plural present deponent indicative of " + entry, getAnswers(presStem + "āminī"), []);
        createQuestion("Third Person Plural Present Deponent Indicative of " + firstPP, "Produce the 3rd person plural present deponent indicative of " + entry, getAnswers(presStem + "antur"), []);
        createQuestion("First Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "ābar"), []);
        createQuestion("Second Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "ābāris")+getAnswers(presStem + "ābāre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "ābātur"), []);
        createQuestion("First Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "ābāmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "ābāminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "ābantur"), []);
        createQuestion("First Person Singular Future Deponent Indicative of " + firstPP, "Produce the 1st person singular future deponent indicative of " + entry, getAnswers(presStem + "ābor"), []);
        createQuestion("Second Person Singular Future Deponent Indicative of " + firstPP, "Produce the 2nd person singular future deponent indicative of " + entry, getAnswers(presStem + "āberis")+getAnswers(presStem + "ābere"), []);
        createQuestion("Third Person Singular Future Deponent Indicative of " + firstPP, "Produce the 3rd person singular future deponent indicative of " + entry, getAnswers(presStem + "ābitur"), []);
        createQuestion("First Person Plural Future Deponent Indicative of " + firstPP, "Produce the 1st person plural future deponent indicative of " + entry, getAnswers(presStem + "ābimur"), []);
        createQuestion("Second Person Plural Future Deponent Indicative of " + firstPP, "Produce the 2nd person plural future deponent indicative of " + entry, getAnswers(presStem + "ābiminī"), []);
        createQuestion("Third Person Plural Future Deponent Indicative of " + firstPP, "Produce the 3rd person plural future deponent indicative of " + entry, getAnswers(presStem + "ābuntur"), []);

    for entry in (secondConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Deponent Indicative of " + firstPP, "Produce the 1st person singular present deponent indicative of " + entry, getAnswers(presStem + "eor"), []);
        createQuestion("Second Person Singular Present Deponent Indicative of " + firstPP, "Produce the 2nd person singular present deponent indicative of " + entry, getAnswers(presStem + "ēris") + getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Present Deponent Indicative of " + firstPP, "Produce the 3rd person singular present deponent indicative of " + entry, getAnswers(presStem + "ētur"), []);
        createQuestion("First Person Plural Present Deponent Indicative of " + firstPP, "Produce the 1st person plural present deponent indicative of " + entry, getAnswers(presStem + "ēmur"), []);
        createQuestion("Second Person Plural Present Deponent Indicative of " + firstPP, "Produce the 2nd person plural present deponent indicative of " + entry, getAnswers(presStem + "ēminī"), []);
        createQuestion("Third Person Plural Present Deponent Indicative of " + firstPP, "Produce the 3rd person plural present deponent indicative of " + entry, getAnswers(presStem + "entur"), []);
        createQuestion("First Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbar"), []);
        createQuestion("Second Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbāris")+getAnswers(presStem + "ēbāre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbātur"), []);
        createQuestion("First Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbāmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbāminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbantur"), []);
        createQuestion("First Person Singular Future Deponent Indicative of " + firstPP, "Produce the 1st person singular future deponent indicative of " + entry, getAnswers(presStem + "ēbor"), []);
        createQuestion("Second Person Singular Future Deponent Indicative of " + firstPP, "Produce the 2nd person singular future deponent indicative of " + entry, getAnswers(presStem + "ēberis")+getAnswers(presStem + "ēbere"), []);
        createQuestion("Third Person Singular Future Deponent Indicative of " + firstPP, "Produce the 3rd person singular future deponent indicative of " + entry, getAnswers(presStem + "ēbitur"), []);
        createQuestion("First Person Plural Future Deponent Indicative of " + firstPP, "Produce the 1st person plural future deponent indicative of " + entry, getAnswers(presStem + "ēbimur"), []);
        createQuestion("Second Person Plural Future Deponent Indicative of " + firstPP, "Produce the 2nd person plural future deponent indicative of " + entry, getAnswers(presStem + "ēbiminī"), []);
        createQuestion("Third Person Plural Future Deponent Indicative of " + firstPP, "Produce the 3rd person plural future deponent indicative of " + entry, getAnswers(presStem + "ēbuntur"), []);

    for entry in (thirdConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Deponent Indicative of " + firstPP, "Produce the 1st person singular present deponent indicative of " + entry, getAnswers(presStem + "or"), []);
        createQuestion("Second Person Singular Present Deponent Indicative of " + firstPP, "Produce the 2nd person singular present deponent indicative of " + entry, getAnswers(presStem + "eris") + getAnswers(presStem + "ere"), []);
        createQuestion("Third Person Singular Present Deponent Indicative of " + firstPP, "Produce the 3rd person singular present deponent indicative of " + entry, getAnswers(presStem + "itur"), []);
        createQuestion("First Person Plural Present Deponent Indicative of " + firstPP, "Produce the 1st person plural present deponent indicative of " + entry, getAnswers(presStem + "imur"), []);
        createQuestion("Second Person Plural Present Deponent Indicative of " + firstPP, "Produce the 2nd person plural present deponent indicative of " + entry, getAnswers(presStem + "iminī"), []);
        createQuestion("Third Person Plural Present Deponent Indicative of " + firstPP, "Produce the 3rd person plural present deponent indicative of " + entry, getAnswers(presStem + "untur"), []);
        createQuestion("First Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbar"), []);
        createQuestion("Second Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbāris")+getAnswers(presStem + "ēbāre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbātur"), []);
        createQuestion("First Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbāmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbāminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "ēbantur"), []);
        createQuestion("First Person Singular Future Deponent Indicative of " + firstPP, "Produce the 1st person singular future deponent indicative of " + entry, getAnswers(presStem + "ar"), []);
        createQuestion("Second Person Singular Future Deponent Indicative of " + firstPP, "Produce the 2nd person singular future deponent indicative of " + entry, getAnswers(presStem + "ēris")+getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Future Deponent Indicative of " + firstPP, "Produce the 3rd person singular future deponent indicative of " + entry, getAnswers(presStem + "ētur"), []);
        createQuestion("First Person Plural Future Deponent Indicative of " + firstPP, "Produce the 1st person plural future deponent indicative of " + entry, getAnswers(presStem + "ēmur"), []);
        createQuestion("Second Person Plural Future Deponent Indicative of " + firstPP, "Produce the 2nd person plural future deponent indicative of " + entry, getAnswers(presStem + "ēminī"), []);
        createQuestion("Third Person Plural Future Deponent Indicative of " + firstPP, "Produce the 3rd person plural future deponent indicative of " + entry, getAnswers(presStem + "entur"), []);

    for entry in (thirdIOConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Deponent Indicative of " + firstPP, "Produce the 1st person singular present deponent indicative of " + entry, getAnswers(presStem + "ior"), []);
        createQuestion("Second Person Singular Present Deponent Indicative of " + firstPP, "Produce the 2nd person singular present deponent indicative of " + entry, getAnswers(presStem + "eris") + getAnswers(presStem + "ere"), []);
        createQuestion("Third Person Singular Present Deponent Indicative of " + firstPP, "Produce the 3rd person singular present deponent indicative of " + entry, getAnswers(presStem + "itur"), []);
        createQuestion("First Person Plural Present Deponent Indicative of " + firstPP, "Produce the 1st person plural present deponent indicative of " + entry, getAnswers(presStem + "imur"), []);
        createQuestion("Second Person Plural Present Deponent Indicative of " + firstPP, "Produce the 2nd person plural present deponent indicative of " + entry, getAnswers(presStem + "iminī"), []);
        createQuestion("Third Person Plural Present Deponent Indicative of " + firstPP, "Produce the 3rd person plural present deponent indicative of " + entry, getAnswers(presStem + "iuntur"), []);
        createQuestion("First Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbar"), []);
        createQuestion("Second Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbāris")+getAnswers(presStem + "iēbāre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbātur"), []);
        createQuestion("First Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbāmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbāminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbantur"), []);
        createQuestion("First Person Singular Future Deponent Indicative of " + firstPP, "Produce the 1st person singular future deponent indicative of " + entry, getAnswers(presStem + "iar"), []);
        createQuestion("Second Person Singular Future Deponent Indicative of " + firstPP, "Produce the 2nd person singular future deponent indicative of " + entry, getAnswers(presStem + "iēris")+getAnswers(presStem + "iēre"), []);
        createQuestion("Third Person Singular Future Deponent Indicative of " + firstPP, "Produce the 3rd person singular future deponent indicative of " + entry, getAnswers(presStem + "iētur"), []);
        createQuestion("First Person Plural Future Deponent Indicative of " + firstPP, "Produce the 1st person plural future deponent indicative of " + entry, getAnswers(presStem + "iēmur"), []);
        createQuestion("Second Person Plural Future Deponent Indicative of " + firstPP, "Produce the 2nd person plural future deponent indicative of " + entry, getAnswers(presStem + "iēminī"), []);
        createQuestion("Third Person Plural Future Deponent Indicative of " + firstPP, "Produce the 3rd person plural future deponent indicative of " + entry, getAnswers(presStem + "ientur"), []);

    for entry in (fourthConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Deponent Indicative of " + firstPP, "Produce the 1st person singular present deponent indicative of " + entry, getAnswers(presStem + "ior"), []);
        createQuestion("Second Person Singular Present Deponent Indicative of " + firstPP, "Produce the 2nd person singular present deponent indicative of " + entry, getAnswers(presStem + "īris") + getAnswers(presStem + "īre"), []);
        createQuestion("Third Person Singular Present Deponent Indicative of " + firstPP, "Produce the 3rd person singular present deponent indicative of " + entry, getAnswers(presStem + "ītur"), []);
        createQuestion("First Person Plural Present Deponent Indicative of " + firstPP, "Produce the 1st person plural present deponent indicative of " + entry, getAnswers(presStem + "īmur"), []);
        createQuestion("Second Person Plural Present Deponent Indicative of " + firstPP, "Produce the 2nd person plural present deponent indicative of " + entry, getAnswers(presStem + "īminī"), []);
        createQuestion("Third Person Plural Present Deponent Indicative of " + firstPP, "Produce the 3rd person plural present deponent indicative of " + entry, getAnswers(presStem + "iuntur"), []);
        createQuestion("First Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbar"), []);
        createQuestion("Second Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbāris")+getAnswers(presStem + "iēbāre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person singular imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbātur"), []);
        createQuestion("First Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 1st person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbāmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 2nd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbāminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Indicative of " + firstPP, "Produce the 3rd person plural imperfect deponent indicative of " + entry, getAnswers(presStem + "iēbantur"), []);
        createQuestion("First Person Singular Future Deponent Indicative of " + firstPP, "Produce the 1st person singular future deponent indicative of " + entry, getAnswers(presStem + "iar"), []);
        createQuestion("Second Person Singular Future Deponent Indicative of " + firstPP, "Produce the 2nd person singular future deponent indicative of " + entry, getAnswers(presStem + "iēris")+getAnswers(presStem + "iēre"), []);
        createQuestion("Third Person Singular Future Deponent Indicative of " + firstPP, "Produce the 3rd person singular future deponent indicative of " + entry, getAnswers(presStem + "iētur"), []);
        createQuestion("First Person Plural Future Deponent Indicative of " + firstPP, "Produce the 1st person plural future deponent indicative of " + entry, getAnswers(presStem + "iēmur"), []);
        createQuestion("Second Person Plural Future Deponent Indicative of " + firstPP, "Produce the 2nd person plural future deponent indicative of " + entry, getAnswers(presStem + "iēminī"), []);
        createQuestion("Third Person Plural Future Deponent Indicative of " + firstPP, "Produce the 3rd person plural future deponent indicative of " + entry, getAnswers(presStem + "ientur"), []);
    
    for entry in (firstConjDep + secondConjDep + thirdConjDep + thirdIOConjDep + fourthConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        stem = fourthPP[:-6];
        createQuestion("First Person Singular Perfect Deponent Indicative of " + firstPP, "Produce the 1st person singular perfect deponent indicative of " + entry, getAnswers(stem + "us sum") + getAnswers(stem + "a sum") + getAnswers(stem + "um sum"), []);
        createQuestion("Second Person Singular Perfect Deponent Indicative of " + firstPP, "Produce the 2nd person singular perfect deponent indicative of " + entry, getAnswers(stem + "us es") + getAnswers(stem + "a es") + getAnswers(stem + "um es"), []);
        createQuestion("Third Person Singular Perfect Deponent Indicative of " + firstPP, "Produce the 3rd person singular perfect deponent indicative of " + entry, getAnswers(stem + "us est") + getAnswers(stem + "a est") + getAnswers(stem + "um est"), []);
        createQuestion("First Person Plural Perfect Deponent Indicative of " + firstPP, "Produce the 1st person plural perfect deponent indicative of " + entry, getAnswers(stem + "ī sumus") + getAnswers(stem + "ae sumus") + getAnswers(stem + "a sumus"), []);
        createQuestion("Second Person Plural Perfect Deponent Indicative of " + firstPP, "Produce the 2nd person plural perfect deponent indicative of " + entry, getAnswers(stem + "ī estis") + getAnswers(stem + "ae estis") + getAnswers(stem + "a estis"), []);
        createQuestion("Third Person Plural Perfect Deponent Indicative of " + firstPP, "Produce the 3rd person plural perfect deponent indicative of " + entry, getAnswers(stem + "ī sunt") + getAnswers(stem + "ae sunt") + getAnswers(stem + "a sunt"), []);
        createQuestion("First Person Singular Pluperfect Deponent Indicative of " + firstPP, "Produce the 1st person singular pluperfect deponent indicative of " + entry, getAnswers(stem + "us eram") + getAnswers(stem + "a eram") + getAnswers(stem + "um eram"), []);
        createQuestion("Second Person Singular Pluperfect Deponent Indicative of " + firstPP, "Produce the 2nd person singular pluperfect deponent indicative of " + entry, getAnswers(stem + "us erās") + getAnswers(stem + "a erās") + getAnswers(stem + "um erās"), []);
        createQuestion("Third Person Singular Pluperfect Deponent Indicative of " + firstPP, "Produce the 3rd person singular pluperfect deponent indicative of " + entry, getAnswers(stem + "us erat") + getAnswers(stem + "a erat") + getAnswers(stem + "um erat"), []);
        createQuestion("First Person Plural Pluperfect Deponent Indicative of " + firstPP, "Produce the 1st person plural pluperfect deponent indicative of " + entry, getAnswers(stem + "ī erāmus") + getAnswers(stem + "ae erāmus") + getAnswers(stem + "a erāmus"), []);
        createQuestion("Second Person Plural Pluperfect Deponent Indicative of " + firstPP, "Produce the 2nd person plural pluperfect deponent indicative of " + entry, getAnswers(stem + "ī erātis") + getAnswers(stem + "ae erātis") + getAnswers(stem + "a erātis"), []);
        createQuestion("Third Person Plural Pluperfect Deponent Indicative of " + firstPP, "Produce the 3rd person plural pluperfect deponent indicative of " + entry, getAnswers(stem + "ī erant") + getAnswers(stem + "ae erant") + getAnswers(stem + "a erant"), []);
        createQuestion("First Person Singular Future Perfect Deponent Indicative of " + firstPP, "Produce the 1st person singular future perfect deponent indicative of " + entry, getAnswers(stem + "us erō") + getAnswers(stem + "a erō") + getAnswers(stem + "um erō"), []);
        createQuestion("Second Person Singular Future Perfect Deponent Indicative of " + firstPP, "Produce the 2nd person singular future perfect deponent indicative of " + entry, getAnswers(stem + "us eris") + getAnswers(stem + "a eris") + getAnswers(stem + "um eris"), []);
        createQuestion("Third Person Singular Future Perfect Deponent Indicative of " + firstPP, "Produce the 3rd person singular future perfect deponent indicative of " + entry, getAnswers(stem + "us erit") + getAnswers(stem + "a erit") + getAnswers(stem + "um erit"), []);
        createQuestion("First Person Plural Future Perfect Deponent Indicative of " + firstPP, "Produce the 1st person plural future perfect deponent indicative of " + entry, getAnswers(stem + "ī erimus") + getAnswers(stem + "ae erimus") + getAnswers(stem + "a erimus"), []);
        createQuestion("Second Person Plural Future Perfect Deponent Indicative of " + firstPP, "Produce the 2nd person plural future perfect deponent indicative of " + entry, getAnswers(stem + "ī eritis") + getAnswers(stem + "ae eritis") + getAnswers(stem + "a eritis"), []);
        createQuestion("Third Person Plural Future Perfect Deponent Indicative of " + firstPP, "Produce the 3rd person plural future perfect deponent indicative of " + entry, getAnswers(stem + "ī erunt") + getAnswers(stem + "ae erunt") + getAnswers(stem + "a erunt"), []);

def createPresSubjQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    global firstConjIntrans;
    global secondConjIntrans;
    global thirdConjIntrans;
    global thirdIOConjIntrans;
    global fourthConjIntrans;

    for entry in (firstConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "em"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "ēs"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "et"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "ēmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "ētis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "ent"), []);
        createQuestion("First Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 1st person singular present passive subjunctive of " + entry, getAnswers(presStem + "er"), []);
        createQuestion("Second Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 2nd person singular present passive subjunctive of " + entry, getAnswers(presStem + "ēris") + getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 3rd person singular present passive subjunctive of " + entry, getAnswers(presStem + "ētur"), []);
        createQuestion("First Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 1st person plural present passive subjunctive of " + entry, getAnswers(presStem + "ēmur"), []);
        createQuestion("Second Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 2nd person plural present passive subjunctive of " + entry, getAnswers(presStem + "ēminī"), []);
        createQuestion("Third Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 3rd person plural present passive subjunctive of " + entry, getAnswers(presStem + "entur"), []);
    for entry in (firstConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "em"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "ēs"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "et"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "ēmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "ētis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "ent"), []);

    for entry in (secondConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "eam"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "eās"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "eat"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "eāmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "eātis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "eant"), []);
        createQuestion("First Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 1st person singular present passive subjunctive of " + entry, getAnswers(presStem + "ear"), []);
        createQuestion("Second Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 2nd person singular present passive subjunctive of " + entry, getAnswers(presStem + "eāris") + getAnswers(presStem + "eāre"), []);
        createQuestion("Third Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 3rd person singular present passive subjunctive of " + entry, getAnswers(presStem + "eātur"), []);
        createQuestion("First Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 1st person plural present passive subjunctive of " + entry, getAnswers(presStem + "eāmur"), []);
        createQuestion("Second Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 2nd person plural present passive subjunctive of " + entry, getAnswers(presStem + "eāminī"), []);
        createQuestion("Third Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 3rd person plural present passive subjunctive of " + entry, getAnswers(presStem + "eantur"), []);
    for entry in (secondConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "eam"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "eās"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "eat"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "eāmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "eātis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "eant"), []);

    for entry in (thirdConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "am"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "ās"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "at"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "āmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "ātis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "ant"), []);
        createQuestion("First Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 1st person singular present passive subjunctive of " + entry, getAnswers(presStem + "ar"), []);
        createQuestion("Second Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 2nd person singular present passive subjunctive of " + entry, getAnswers(presStem + "āris") + getAnswers(presStem + "āre"), []);
        createQuestion("Third Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 3rd person singular present passive subjunctive of " + entry, getAnswers(presStem + "ātur"), []);
        createQuestion("First Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 1st person plural present passive subjunctive of " + entry, getAnswers(presStem + "āmur"), []);
        createQuestion("Second Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 2nd person plural present passive subjunctive of " + entry, getAnswers(presStem + "āminī"), []);
        createQuestion("Third Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 3rd person plural present passive subjunctive of " + entry, getAnswers(presStem + "antur"), []);
    for entry in (thirdConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "am"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "ās"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "at"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "āmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "ātis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "ant"), []);

    for entry in (thirdIOConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "iam"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "iās"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "iat"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "iāmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "iātis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "iant"), []);
        if (firstPP != "faciō"):
            createQuestion("First Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 1st person singular present passive subjunctive of " + entry, getAnswers(presStem + "iar"), []);
            createQuestion("Second Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 2nd person singular present passive subjunctive of " + entry, getAnswers(presStem + "iāris") + getAnswers(presStem + "iāre"), []);
            createQuestion("Third Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 3rd person singular present passive subjunctive of " + entry, getAnswers(presStem + "iātur"), []);
            createQuestion("First Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 1st person plural present passive subjunctive of " + entry, getAnswers(presStem + "iāmur"), []);
            createQuestion("Second Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 2nd person plural present passive subjunctive of " + entry, getAnswers(presStem + "iāminī"), []);
            createQuestion("Third Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 3rd person plural present passive subjunctive of " + entry, getAnswers(presStem + "iantur"), []);
    for entry in (thirdIOConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "iam"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "iās"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "iat"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "iāmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "iātis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "iant"), []);

    for entry in (fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "iam"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "iās"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "iat"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "iāmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "iātis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "iant"), []);
        createQuestion("First Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 1st person singular present passive subjunctive of " + entry, getAnswers(presStem + "iar"), []);
        createQuestion("Second Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 2nd person singular present passive subjunctive of " + entry, getAnswers(presStem + "iāris") + getAnswers(presStem + "iāre"), []);
        createQuestion("Third Person Singular Present Passive Subjunctive of " + firstPP, "Produce the 3rd person singular present passive subjunctive of " + entry, getAnswers(presStem + "iātur"), []);
        createQuestion("First Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 1st person plural present passive subjunctive of " + entry, getAnswers(presStem + "iāmur"), []);
        createQuestion("Second Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 2nd person plural present passive subjunctive of " + entry, getAnswers(presStem + "iāminī"), []);
        createQuestion("Third Person Plural Present Passive Subjunctive of " + firstPP, "Produce the 3rd person plural present passive subjunctive of " + entry, getAnswers(presStem + "iantur"), []);
    for entry in (fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("First Person Singular Present Active Subjunctive of " + firstPP, "Produce the 1st person singular present active subjunctive of " + entry, getAnswers(presStem + "iam"), []);
        createQuestion("Second Person Singular Present Active Subjunctive of " + firstPP, "Produce the 2nd person singular present active subjunctive of " + entry, getAnswers(presStem + "iās"), []);
        createQuestion("Third Person Singular Present Active Subjunctive of " + firstPP, "Produce the 3rd person singular present active subjunctive of " + entry, getAnswers(presStem + "iat"), []);
        createQuestion("First Person Plural Present Active Subjunctive of " + firstPP, "Produce the 1st person plural present active subjunctive of " + entry, getAnswers(presStem + "iāmus"), []);
        createQuestion("Second Person Plural Present Active Subjunctive of " + firstPP, "Produce the 2nd person plural present active subjunctive of " + entry, getAnswers(presStem + "iātis"), []);
        createQuestion("Third Person Plural Present Active Subjunctive of " + firstPP, "Produce the 3rd person plural present active subjunctive of " + entry, getAnswers(presStem + "iant"), []);

def createImpfSubjQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    global firstConjIntrans;
    global secondConjIntrans;
    global thirdConjIntrans;
    global thirdIOConjIntrans;
    global fourthConjIntrans;

    for entry in (firstConjTrans + secondConjTrans + thirdConjTrans + thirdIOConjTrans + fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        createQuestion("First Person Singular Imperfect Active Subjunctive of " + firstPP, "Produce the 1st person singular imperfect active subjunctive of " + entry, getAnswers(presStem + "em"), []);
        createQuestion("Second Person Singular Imperfect Active Subjunctive of " + firstPP, "Produce the 2nd person singular imperfect active subjunctive of " + entry, getAnswers(presStem + "ēs"), []);
        createQuestion("Third Person Singular Imperfect Active Subjunctive of " + firstPP, "Produce the 3rd person singular imperfect active subjunctive of " + entry, getAnswers(presStem + "et"), []);
        createQuestion("First Person Plural Imperfect Active Subjunctive of " + firstPP, "Produce the 1st person plural imperfect active subjunctive of " + entry, getAnswers(presStem + "ēmus"), []);
        createQuestion("Second Person Plural Imperfect Active Subjunctive of " + firstPP, "Produce the 2nd person plural imperfect active subjunctive of " + entry, getAnswers(presStem + "ētis"), []);
        createQuestion("Third Person Plural Imperfect Active Subjunctive of " + firstPP, "Produce the 3rd person plural imperfect active subjunctive of " + entry, getAnswers(presStem + "ent"), []);
        if firstPP != "faciō":
            createQuestion("First Person Singular Imperfect Passive Subjunctive of " + firstPP, "Produce the 1st person singular imperfect passive subjunctive of " + entry, getAnswers(presStem + "er"), []);
            createQuestion("Second Person Singular Imperfect Passive Subjunctive of " + firstPP, "Produce the 2nd person singular imperfect passive subjunctive of " + entry, getAnswers(presStem + "ēris") + getAnswers(presStem + "ēre"), []);
            createQuestion("Third Person Singular Imperfect Passive Subjunctive of " + firstPP, "Produce the 3rd person singular imperfect passive subjunctive of " + entry, getAnswers(presStem + "ētur"), []);
            createQuestion("First Person Plural Imperfect Passive Subjunctive of " + firstPP, "Produce the 1st person plural imperfect passive subjunctive of " + entry, getAnswers(presStem + "ēmur"), []);
            createQuestion("Second Person Plural Imperfect Passive Subjunctive of " + firstPP, "Produce the 2nd person plural imperfect passive subjunctive of " + entry, getAnswers(presStem + "ēminī"), []);
            createQuestion("Third Person Plural Imperfect Passive Subjunctive of " + firstPP, "Produce the 3rd person plural imperfect passive subjunctive of " + entry, getAnswers(presStem + "entur"), []);
    for entry in (firstConjIntrans + secondConjIntrans + thirdConjIntrans + thirdIOConjIntrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        createQuestion("First Person Singular Imperfect Active Subjunctive of " + firstPP, "Produce the 1st person singular imperfect active subjunctive of " + entry, getAnswers(presStem + "em"), []);
        createQuestion("Second Person Singular Imperfect Active Subjunctive of " + firstPP, "Produce the 2nd person singular imperfect active subjunctive of " + entry, getAnswers(presStem + "ēs"), []);
        createQuestion("Third Person Singular Imperfect Active Subjunctive of " + firstPP, "Produce the 3rd person singular imperfect active subjunctive of " + entry, getAnswers(presStem + "et"), []);
        createQuestion("First Person Plural Imperfect Active Subjunctive of " + firstPP, "Produce the 1st person plural imperfect active subjunctive of " + entry, getAnswers(presStem + "ēmus"), []);
        createQuestion("Second Person Plural Imperfect Active Subjunctive of " + firstPP, "Produce the 2nd person plural imperfect active subjunctive of " + entry, getAnswers(presStem + "ētis"), []);
        createQuestion("Third Person Plural Imperfect Active Subjunctive of " + firstPP, "Produce the 3rd person plural imperfect active subjunctive of " + entry, getAnswers(presStem + "ent"), []);

def createPerfActSubjQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    global firstConjIntrans;
    global secondConjIntrans;
    global thirdConjIntrans;
    global thirdIOConjIntrans;
    global fourthConjIntrans;

    for entry in (firstConjTrans + secondConjTrans + thirdConjTrans + thirdIOConjTrans + fourthConjTrans + firstConjIntrans + secondConjIntrans + thirdConjIntrans + thirdIOConjIntrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        strippedPerfStems = [(x.strip())[:-1] for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Perfect Active Subjunctive of " + firstPP, "Produce the 1st person singular perfect active subjunctive of " + entry, [getAnswers(x + "erim") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Singular Perfect Active Subjunctive of " + firstPP, "Produce the 2nd person singular perfect active subjunctive of " + entry, [getAnswers(x + "erīs") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Singular Perfect Active Subjunctive of " + firstPP, "Produce the 3rd person singular perfect active subjunctive of " + entry, [getAnswers(x + "erit") for x in strippedPerfStems][0], []);
        createQuestion("First Person Plural Perfect Active Subjunctive of " + firstPP, "Produce the 1st person plural perfect active subjunctive of " + entry, [getAnswers(x + "erīmus") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Plural Perfect Active Subjunctive of " + firstPP, "Produce the 2nd person plural perfect active subjunctive of " + entry, [getAnswers(x + "erītis") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Plural Perfect Active Subjunctive of " + firstPP, "Produce the 3rd person plural perfect active subjunctive of " + entry, [getAnswers(x + "erint") for x in strippedPerfStems][0], []);

def createPlpfActSubjQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    global firstConjIntrans;
    global secondConjIntrans;
    global thirdConjIntrans;
    global thirdIOConjIntrans;
    global fourthConjIntrans;

    for entry in (firstConjTrans + secondConjTrans + thirdConjTrans + thirdIOConjTrans + fourthConjTrans + firstConjIntrans + secondConjIntrans + thirdConjIntrans + thirdIOConjIntrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        strippedPerfStems = [(x.strip())[:-1] for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("First Person Singular Pluperfect Active Subjunctive of " + firstPP, "Produce the 1st person singular pluperfect active subjunctive of " + entry, [getAnswers(x + "issem") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Singular Pluperfect Active Subjunctive of " + firstPP, "Produce the 2nd person singular pluperfect active subjunctive of " + entry, [getAnswers(x + "issēs") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Singular Pluperfect Active Subjunctive of " + firstPP, "Produce the 3rd person singular pluperfect active subjunctive of " + entry, [getAnswers(x + "isset") for x in strippedPerfStems][0], []);
        createQuestion("First Person Plural Pluperfect Active Subjunctive of " + firstPP, "Produce the 1st person plural pluperfect active subjunctive of " + entry, [getAnswers(x + "issēmus") for x in strippedPerfStems][0], []);
        createQuestion("Second Person Plural Pluperfect Active Subjunctive of " + firstPP, "Produce the 2nd person plural pluperfect active subjunctive of " + entry, [getAnswers(x + "issētis") for x in strippedPerfStems][0], []);
        createQuestion("Third Person Plural Pluperfect Active Subjunctive of " + firstPP, "Produce the 3rd person plural pluperfect active subjunctive of " + entry, [getAnswers(x + "issent") for x in strippedPerfStems][0], []);

def createPerfPassSubjQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;

    for entry in (firstConjTrans + secondConjTrans + thirdConjTrans + thirdIOConjTrans + fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        fourthPP = strippedEntry[3];
        stem = fourthPP[:-2];
       
        createQuestion("First Person Singular Perfect Passive Subjunctive of " + firstPP, "Produce the 1st person singular perfect passive subjunctive of " + entry, getAnswers(stem + "us sim") + getAnswers(stem + "a sim") + getAnswers(stem + "um sim"), []);
        createQuestion("Second Person Singular Perfect Passive Subjunctive of " + firstPP, "Produce the 2nd person singular perfect passive subjunctive of " + entry, getAnswers(stem + "us sīs") + getAnswers(stem + "a sīs") + getAnswers(stem + "um sīs"), []);
        createQuestion("Third Person Singular Perfect Passive Subjunctive of " + firstPP, "Produce the 3rd person singular perfect passive subjunctive of " + entry, getAnswers(stem + "us sit") + getAnswers(stem + "a sit") + getAnswers(stem + "um sit"), []);
        createQuestion("First Person Plural Perfect Passive Subjunctive of " + firstPP, "Produce the 1st person plural perfect passive subjunctive of " + entry, getAnswers(stem + "ī sīmus") + getAnswers(stem + "ae sīmus") + getAnswers(stem + "a sīmus"), []);
        createQuestion("Second Person Plural Perfect Passive Subjunctive of " + firstPP, "Produce the 2nd person plural perfect passive subjunctive of " + entry, getAnswers(stem + "ī sītis") + getAnswers(stem + "ae sītis") + getAnswers(stem + "a sītis"), []);
        createQuestion("Third Person Plural Perfect Passive Subjunctive of " + firstPP, "Produce the 3rd person plural perfect passive subjunctive of " + entry, getAnswers(stem + "ī sint") + getAnswers(stem + "ae sint") + getAnswers(stem + "a sint"), []);

def createPlpfPassSubjQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;

    for entry in (firstConjTrans + secondConjTrans + thirdConjTrans + thirdIOConjTrans + fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        thirdPP = strippedEntry[2];
        fourthPP = strippedEntry[3];
        stem = fourthPP[:-2];
       
        createQuestion("First Person Singular Pluperfect Passive Subjunctive of " + firstPP, "Produce the 1st person singular pluperfect passive subjunctive of " + entry, getAnswers(stem + "us essem") + getAnswers(stem + "a essem") + getAnswers(stem + "um essem"), []);
        createQuestion("Second Person Singular Pluperfect Passive Subjunctive of " + firstPP, "Produce the 2nd person singular pluperfect passive subjunctive of " + entry, getAnswers(stem + "us essēs") + getAnswers(stem + "a essēs") + getAnswers(stem + "um essēs"), []);
        createQuestion("Third Person Singular Pluperfect Passive Subjunctive of " + firstPP, "Produce the 3rd person singular pluperfect passive subjunctive of " + entry, getAnswers(stem + "us esset") + getAnswers(stem + "a esset") + getAnswers(stem + "um esset"), []);
        createQuestion("First Person Plural Pluperfect Passive Subjunctive of " + firstPP, "Produce the 1st person plural pluperfect passive subjunctive of " + entry, getAnswers(stem + "ī essēmus") + getAnswers(stem + "ae essēmus") + getAnswers(stem + "a essēmus"), []);
        createQuestion("Second Person Plural Pluperfect Passive Subjunctive of " + firstPP, "Produce the 2nd person plural pluperfect passive subjunctive of " + entry, getAnswers(stem + "ī essētis") + getAnswers(stem + "ae essētis") + getAnswers(stem + "a essētis"), []);
        createQuestion("Third Person Plural Pluperfect Passive Subjunctive of " + firstPP, "Produce the 3rd person plural pluperfect passive subjunctive of " + entry, getAnswers(stem + "ī essent") + getAnswers(stem + "ae essent") + getAnswers(stem + "a essent"), []);

def createDeponentSubjQuestions():
    global firstConjDep;
    global secondConjDep;
    global thirdConjDep;
    global thirdIOConjDep;
    global fourthConjDep;

    for entry in (firstConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        stem = secondPP[:-1];
        createQuestion("First Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 1st person singular present deponent subjunctive of " + entry, getAnswers(presStem + "er"), []);
        createQuestion("Second Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "ēris") + getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "ētur"), []);
        createQuestion("First Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 1st person plural present deponent subjunctive of " + entry, getAnswers(presStem + "ēmur"), []);
        createQuestion("Second Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "ēminī"), []);
        createQuestion("Third Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "entur"), []);
        createQuestion("First Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "er"), []);
        createQuestion("Second Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēris") + getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ētur"), []);
        createQuestion("First Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "entur"), []);
        
    for entry in (secondConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        stem = secondPP[:-1];
        createQuestion("First Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 1st person singular present deponent subjunctive of " + entry, getAnswers(presStem + "ear"), []);
        createQuestion("Second Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "eāris") + getAnswers(presStem + "eāre"), []);
        createQuestion("Third Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "eātur"), []);
        createQuestion("First Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 1st person plural present deponent subjunctive of " + entry, getAnswers(presStem + "eāmur"), []);
        createQuestion("Second Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "eāminī"), []);
        createQuestion("Third Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "eantur"), []);
        createQuestion("First Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "er"), []);
        createQuestion("Second Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēris") + getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ētur"), []);
        createQuestion("First Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "entur"), []);
    
    for entry in (thirdConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        stem = secondPP[:-1] + "er";
        createQuestion("First Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 1st person singular present deponent subjunctive of " + entry, getAnswers(presStem + "ar"), []);
        createQuestion("Second Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "āris") + getAnswers(presStem + "āre"), []);
        createQuestion("Third Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "ātur"), []);
        createQuestion("First Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 1st person plural present deponent subjunctive of " + entry, getAnswers(presStem + "āmur"), []);
        createQuestion("Second Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "āminī"), []);
        createQuestion("Third Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "antur"), []);
        createQuestion("First Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "er"), []);
        createQuestion("Second Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēris") + getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ētur"), []);
        createQuestion("First Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "entur"), []);

    for entry in (thirdIOConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        stem = secondPP[:-1] + "er";
        createQuestion("First Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 1st person singular present deponent subjunctive of " + entry, getAnswers(presStem + "iar"), []);
        createQuestion("Second Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "iāris") + getAnswers(presStem + "iāre"), []);
        createQuestion("Third Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "iātur"), []);
        createQuestion("First Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 1st person plural present deponent subjunctive of " + entry, getAnswers(presStem + "iāmur"), []);
        createQuestion("Second Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "iāminī"), []);
        createQuestion("Third Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "iantur"), []);
        createQuestion("First Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "er"), []);
        createQuestion("Second Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēris") + getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ētur"), []);
        createQuestion("First Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "entur"), []);
   
    for entry in (fourthConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        stem = secondPP[:-1];
        createQuestion("First Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 1st person singular present deponent subjunctive of " + entry, getAnswers(presStem + "iar"), []);
        createQuestion("Second Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "iāris") + getAnswers(presStem + "iāre"), []);
        createQuestion("Third Person Singular Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular present deponent subjunctive of " + entry, getAnswers(presStem + "iātur"), []);
        createQuestion("First Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 1st person plural present deponent subjunctive of " + entry, getAnswers(presStem + "iāmur"), []);
        createQuestion("Second Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "iāminī"), []);
        createQuestion("Third Person Plural Present Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural present deponent subjunctive of " + entry, getAnswers(presStem + "iantur"), []);
        createQuestion("First Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "er"), []);
        createQuestion("Second Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēris") + getAnswers(presStem + "ēre"), []);
        createQuestion("Third Person Singular Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular imperfect deponent subjunctive of " + entry, getAnswers(stem + "ētur"), []);
        createQuestion("First Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēmur"), []);
        createQuestion("Second Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "ēminī"), []);
        createQuestion("Third Person Plural Imperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural imperfect deponent subjunctive of " + entry, getAnswers(stem + "entur"), []);

    for entry in (firstConjDep + secondConjDep + thirdConjDep + thirdIOConjDep + fourthConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        fourthPP = strippedEntry[2];
        stem = fourthPP[:-6];
        createQuestion("First Person Singular Perfect Deponent Subjunctive of " + firstPP, "Produce the 1st person singular perfect deponent subjunctive of " + entry, getAnswers(stem + "us sim") + getAnswers(stem + "a sim") + getAnswers(stem + "um sim"), []);
        createQuestion("Second Person Singular Perfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular perfect deponent subjunctive of " + entry, getAnswers(stem + "us sīs") + getAnswers(stem + "a sīs") + getAnswers(stem + "um sīs"), []);
        createQuestion("Third Person Singular Perfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular perfect deponent subjunctive of " + entry, getAnswers(stem + "us sit") + getAnswers(stem + "a sit") + getAnswers(stem + "um sit"), []);
        createQuestion("First Person Plural Perfect Deponent Subjunctive of " + firstPP, "Produce the 1st person plural perfect deponent subjunctive of " + entry, getAnswers(stem + "ī sīmus") + getAnswers(stem + "ae sīmus") + getAnswers(stem + "a sīmus"), []);
        createQuestion("Second Person Plural Perfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural perfect deponent subjunctive of " + entry, getAnswers(stem + "ī sītis") + getAnswers(stem + "ae sītis") + getAnswers(stem + "a sītis"), []);
        createQuestion("Third Person Plural Perfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural perfect deponent subjunctive of " + entry, getAnswers(stem + "ī sint") + getAnswers(stem + "ae sint") + getAnswers(stem + "a sint"), []);
        createQuestion("First Person Singular Pluperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person singular pluperfect deponent subjunctive of " + entry, getAnswers(stem + "us essem") + getAnswers(stem + "a essem") + getAnswers(stem + "um essem"), []);
        createQuestion("Second Person Singular Pluperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person singular pluperfect deponent subjunctive of " + entry, getAnswers(stem + "us essēs") + getAnswers(stem + "a essēs") + getAnswers(stem + "um essēs"), []);
        createQuestion("Third Person Singular Pluperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person singular pluperfect deponent subjunctive of " + entry, getAnswers(stem + "us esset") + getAnswers(stem + "a esset") + getAnswers(stem + "um esset"), []);
        createQuestion("First Person Plural Pluperfect Deponent Subjunctive of " + firstPP, "Produce the 1st person plural pluperfect deponent subjunctive of " + entry, getAnswers(stem + "ī essēmus") + getAnswers(stem + "ae essēmus") + getAnswers(stem + "a essēmus"), []);
        createQuestion("Second Person Plural Pluperfect Deponent Subjunctive of " + firstPP, "Produce the 2nd person plural pluperfect deponent subjunctive of " + entry, getAnswers(stem + "ī essētis") + getAnswers(stem + "ae essētis") + getAnswers(stem + "a essētis"), []);
        createQuestion("Third Person Plural Pluperfect Deponent Subjunctive of " + firstPP, "Produce the 3rd person plural pluperfect deponent subjunctive of " + entry, getAnswers(stem + "ī essent") + getAnswers(stem + "ae essent") + getAnswers(stem + "a essent"), []);

def createImperativeQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    global firstConjIntrans;
    global secondConjIntrans;
    global thirdConjIntrans;
    global thirdIOConjIntrans;
    global fourthConjIntrans;

    for entry in (firstConjTrans + firstConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Second Person Singular Present Active Imperative of " + firstPP, "Produce the 2nd person singular present active imperative of " + entry, getAnswers(presStem + "ā"), []);
        createQuestion("Second Person Plural Present Active Imperative of " + firstPP, "Produce the 2nd person plural present active imperative of " + entry, getAnswers(presStem + "āte"), []);
    for entry in (secondConjTrans + secondConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Second Person Singular Present Active Imperative of " + firstPP, "Produce the 2nd person singular present active imperative of " + entry, getAnswers(presStem + "ē"), []);
        createQuestion("Second Person Plural Present Active Imperative of " + firstPP, "Produce the 2nd person plural present active imperative of " + entry, getAnswers(presStem + "ēte"), []);
    for entry in (thirdConjTrans + thirdConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if(firstPP == "dīcō"):
            createQuestion("Second Person Singular Present Active Imperative of " + firstPP, "Produce the 2nd person singular present active imperative of " + entry, getAnswers(presStem), []);
            createQuestion("Second Person Plural Present Active Imperative of " + firstPP, "Produce the 2nd person plural present active imperative of " + entry, getAnswers(presStem + "ite"), []);
        elif(firstPP == "dūcō"):
            createQuestion("Second Person Singular Present Active Imperative of " + firstPP, "Produce the 2nd person singular present active imperative of " + entry, getAnswers(presStem), []);
            createQuestion("Second Person Plural Present Active Imperative of " + firstPP, "Produce the 2nd person plural present active imperative of " + entry, getAnswers(presStem + "ite"), []);
        else:
            createQuestion("Second Person Singular Present Active Imperative of " + firstPP, "Produce the 2nd person singular present active imperative of " + entry, getAnswers(presStem + "e"), []);
            createQuestion("Second Person Plural Present Active Imperative of " + firstPP, "Produce the 2nd person plural present active imperative of " + entry, getAnswers(presStem + "ite"), []);
    for entry in (thirdIOConjTrans + thirdIOConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if(firstPP == "faciō"):
            createQuestion("Second Person Singular Present Active Imperative of " + firstPP, "Produce the 2nd person singular present active imperative of " + entry, getAnswers(presStem), []);
            createQuestion("Second Person Plural Present Active Imperative of " + firstPP, "Produce the 2nd person plural present active imperative of " + entry, getAnswers(presStem + "ite"), []);
        else:
            createQuestion("Second Person Singular Present Active Imperative of " + firstPP, "Produce the 2nd person singular present active imperative of " + entry, getAnswers(presStem + "e"), []);
            createQuestion("Second Person Plural Present Active Imperative of " + firstPP, "Produce the 2nd person plural present active imperative of " + entry, getAnswers(presStem + "ite"), []);
    for entry in (fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Second Person Singular Present Active Imperative of " + firstPP, "Produce the 2nd person singular present active imperative of " + entry, getAnswers(presStem + "ī"), []);
        createQuestion("Second Person Plural Present Active Imperative of " + firstPP, "Produce the 2nd person plural present active imperative of " + entry, getAnswers(presStem + "īte"), []);

def createDeponentImperativeQuestions():
    global firstConjDep;
    global secondConjDep;
    global thirdConjDep;
    global thirdIOConjDep;
    global fourthConjDep;

    for entry in (firstConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Second Person Singular Present Deponent Imperative of " + firstPP, "Produce the 2nd person singular present deponent imperative of " + entry, getAnswers(presStem + "āre"), []);
        createQuestion("Second Person Plural Present Deponent Imperative of " + firstPP, "Produce the 2nd person plural present deponent imperative of " + entry, getAnswers(presStem + "āminī"), []);
    for entry in (secondConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Second Person Singular Present Deponent Imperative of " + firstPP, "Produce the 2nd person singular present deponent imperative of " + entry, getAnswers(presStem + "ēre"), []);
        createQuestion("Second Person Plural Present Deponent Imperative of " + firstPP, "Produce the 2nd person plural present deponent imperative of " + entry, getAnswers(presStem + "ēminī"), []);
    for entry in (thirdConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        createQuestion("Second Person Singular Present Deponent Imperative of " + firstPP, "Produce the 2nd person singular present deponent imperative of " + entry, getAnswers(presStem + "ere"), []);
        createQuestion("Second Person Plural Present Deponent Imperative of " + firstPP, "Produce the 2nd person plural present deponent imperative of " + entry, getAnswers(presStem + "iminī"), []);
    for entry in (thirdIOConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        createQuestion("Second Person Singular Present Deponent Imperative of " + firstPP, "Produce the 2nd person singular present deponent imperative of " + entry, getAnswers(presStem + "ere"), []);
        createQuestion("Second Person Plural Present Deponent Imperative of " + firstPP, "Produce the 2nd person plural present deponent imperative of " + entry, getAnswers(presStem + "iminī"), []);
    for entry in (fourthConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Second Person Singular Present Deponent Imperative of " + firstPP, "Produce the 2nd person singular present deponent imperative of " + entry, getAnswers(presStem + "īre"), []);
        createQuestion("Second Person Plural Present Deponent Imperative of " + firstPP, "Produce the 2nd person plural present deponent imperative of " + entry, getAnswers(presStem + "īminī"), []);

def createInfinitiveQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    global firstConjIntrans;
    global secondConjIntrans;
    global thirdConjIntrans;
    global thirdIOConjIntrans;
    global fourthConjIntrans;

    for entry in (firstConjTrans + firstConjIntrans + secondConjTrans + secondConjIntrans + thirdConjTrans + thirdConjIntrans + thirdIOConjTrans + thirdIOConjIntrans + fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedPerfStems = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("Present Active Infinitive of " + firstPP, "Produce the present active infinitive of " + entry, getAnswers(secondPP), []);
        createQuestion("Perfect Active Infinitive of " + firstPP, "Produce the perfect active infinitive of " + entry, [getAnswers(x[:-1] + "isse") for x in strippedPerfStems][0], []);
        if (fourthPP != "-"):
            if (fourthPP[-4:] == "ūrus"):
                createQuestion("Future Active Infinitive of " + firstPP, "Produce the future active infinitive of " + entry, getAnswers(fourthPP + " esse"), []);
            else:
                createQuestion("Future Active Infinitive of " + firstPP, "Produce the future active infinitive of " + entry, getAnswers(fourthPP[:-2] + "ūrus esse"), []);

    for entry in (firstConjTrans + secondConjTrans + fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        createQuestion("Present Passive Infinitive of " + firstPP, "Produce the present passive infinitive of " + entry, getAnswers(presStem + "ī"), []);
        if (fourthPP != "-" and fourthPP[-4:] != "ūrus"):
            createQuestion("Perfect Passive Infinitive of " + firstPP, "Produce the perfect passive infinitive of " + entry, getAnswers(fourthPP + " esse"), []);

    for entry in (thirdConjTrans + thirdIOConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        if(firstPP != "faciō"):
            createQuestion("Present Passive Infinitive of " + firstPP, "Produce the present passive infinitive of " + entry, getAnswers(presStem + "ī"), []);
        if (fourthPP != "-" and fourthPP[-4:] != "ūrus"):
            createQuestion("Perfect Passive Infinitive of " + firstPP, "Produce the perfect passive infinitive of " + entry, getAnswers(fourthPP + " esse"), []);

def createDeponentInfinitiveQuestions():
    global firstConjDep;
    global secondConjDep;
    global thirdConjDep;
    global thirdIOConjDep;
    global fourthConjDep;

    for entry in (firstConjDep + secondConjDep + thirdConjDep + thirdIOConjDep + fourthConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        createQuestion("Present Deponent Infinitive of " + firstPP, "Produce the present deponent infinitive of " + entry, getAnswers(secondPP), []);
        if (fourthPP != "-"):
            if (fourthPP[-8:] == "ūrus sum"):
                    createQuestion("Future Deponent Infinitive of " + firstPP, "Produce the future deponent (active) infinitive of " + entry, getAnswers(fourthPP[:-4] + " esse"), []);
            else:
                    createQuestion("Future Deponent Infinitive of " + firstPP, "Produce the future deponent (active) infinitive of " + entry, getAnswers(fourthPP[:-4] + "ūrus esse"), []);
                    createQuestion("Perfect Deponent Infinitive of " + firstPP, "Produce the perfect deponent infinitive of " + entry, getAnswers(fourthPP[:-4] + " esse"), []);

def createParticipleQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    global firstConjIntrans;
    global secondConjIntrans;
    global thirdConjIntrans;
    global thirdIOConjIntrans;
    global fourthConjIntrans;

    for entry in (firstConjTrans + firstConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Present Active Participle of " + firstPP, "Produce the present active masculine nominative singular participle of " + entry, getAnswers(secondPP[:-3] + "āns"), []);

    for entry in (secondConjTrans + secondConjIntrans + thirdConjTrans + thirdConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Present Active Participle of " + firstPP, "Produce the present active masculine nominative singular participle of " + entry, getAnswers(secondPP[:-3] + "ēns"), []);

    for entry in (thirdIOConjTrans + thirdIOConjIntrans + fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Present Active Participle of " + firstPP, "Produce the present active masculine nominative singular participle of " + entry, getAnswers(secondPP[:-3] + "iēns"), []);
    
    for entry in (firstConjTrans + firstConjIntrans + secondConjTrans + secondConjIntrans + thirdConjTrans + thirdConjIntrans + thirdIOConjTrans + thirdIOConjIntrans + fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        thirdPP = strippedEntry[2];
        strippedThirdPP = [x.strip() for x in thirdPP.split("/")];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        if (fourthPP != "-"):
            if (fourthPP[-4:] == "ūrus"):
                createQuestion("Future Active Participle of " + firstPP, "Produce the future active masculine nominative singular participle of " + entry, getAnswers(fourthPP), []);
            else:
                createQuestion("Future Active Participle of " + firstPP, "Produce the future active masculine nominative singular participle of " + entry, getAnswers(fourthPP[:-2] + "ūrus"), []);

    for entry in (firstConjTrans + secondConjTrans + thirdConjTrans + thirdIOConjTrans + fourthConjTrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        if len(strippedEntry) == 5:
            fourthPP = strippedEntry[3];
            meaning = strippedEntry[4];
        else:
            fourthPP = "-";
            meaning = strippedEntry[3];
        if (fourthPP != "-" and fourthPP[-4:] != "ūrus"):
            createQuestion("Perfect Passive Participle of " + firstPP, "Produce the perfect passive masculine nominative singular participle of " + entry, getAnswers(fourthPP), []);

def createDeponentParticipleQuestions():
    global firstConjDep;
    global secondConjDep;
    global thirdConjDep;
    global thirdIOConjDep;
    global fourthConjDep;

    for entry in (firstConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Present Deponent Participle of " + firstPP, "Produce the present deponent masculine nominative singular participle of " + entry, getAnswers(secondPP[:-3] + "āns"), []);

    for entry in (secondConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Present Deponent Participle of " + firstPP, "Produce the present deponent masculine nominative singular participle of " + entry, getAnswers(secondPP[:-3] + "ēns"), []);

    for entry in (thirdConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        createQuestion("Present Deponent Participle of " + firstPP, "Produce the present deponent masculine nominative singular participle of " + entry, getAnswers(secondPP[:-1] + "ēns"), []);

    for entry in (thirdIOConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        createQuestion("Present Deponent Participle of " + firstPP, "Produce the present deponent masculine nominative singular participle of " + entry, getAnswers(secondPP[:-1] + "iēns"), []);

    for entry in (fourthConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Present Deponent Participle of " + firstPP, "Produce the present deponent masculine nominative singular participle of " + entry, getAnswers(secondPP[:-3] + "iēns"), []);
    
    for entry in (firstConjDep + secondConjDep + thirdConjDep + thirdIOConjDep + fourthConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        if len(strippedEntry) == 4:
            fourthPP = strippedEntry[2];
            meaning = strippedEntry[3];
        else:
            fourthPP = "-";
            meaning = strippedEntry[2];
        if (fourthPP != "-"):
            if (fourthPP[-8:] == "ūrus sum"):
                createQuestion("Future Deponent Participle of " + firstPP, "Produce the future deponent (active) masculine nominative singular participle of " + entry, getAnswers(fourthPP[:-4]), []);
            else:
                createQuestion("Perfect Deponent Participle of " + firstPP, "Produce the perfect deponent masculine nominative singular participle of " + entry, getAnswers(fourthPP[:-4]), []);
                createQuestion("Future Deponent Participle of " + firstPP, "Produce the future deponent (active) masculine nominative singular participle of " + entry, getAnswers(fourthPP[:-6] + "ūrus"), []);

def createGerundiveQuestions():
    global firstConjTrans;
    global secondConjTrans;
    global thirdConjTrans;
    global thirdIOConjTrans;
    global fourthConjTrans;
    global firstConjIntrans;
    global secondConjIntrans;
    global thirdConjIntrans;
    global thirdIOConjIntrans;
    global fourthConjIntrans;

    for entry in (firstConjTrans + firstConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Gerundive of " + firstPP, "Produce the masculine nominative singular gerundive of " + entry, getAnswers(secondPP[:-3] + "andus"), []);

    for entry in (secondConjTrans + secondConjIntrans + thirdConjTrans + thirdConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Gerundive of " + firstPP, "Produce the masculine nominative singular gerundive of " + entry, getAnswers(secondPP[:-3] + "endus"), []);

    for entry in (thirdIOConjTrans + thirdIOConjIntrans + fourthConjTrans + fourthConjIntrans):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Gerundive of " + firstPP, "Produce the masculine nominative singular gerundive of " + entry, getAnswers(secondPP[:-3] + "iendus"), []);
    
def createDeponentGerundiveQuestions():
    global firstConjDep;
    global secondConjDep;
    global thirdConjDep;
    global thirdIOConjDep;
    global fourthConjDep;

    for entry in (firstConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Gerundive of " + firstPP, "Produce the masculine nominative singular gerundive of " + entry, getAnswers(secondPP[:-3] + "andus"), []);

    for entry in (secondConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Gerundive of " + firstPP, "Produce the masculine nominative singular gerundive of " + entry, getAnswers(secondPP[:-3] + "endus"), []);

    for entry in (thirdConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        createQuestion("Gerundive of " + firstPP, "Produce the masculine nominative singular gerundive of " + entry, getAnswers(secondPP[:-1] + "endus"), []);

    for entry in (thirdIOConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-1];
        createQuestion("Gerundive of " + firstPP, "Produce the masculine nominative singular gerundive of " + entry, getAnswers(secondPP[:-1] + "iendus"), []);

    for entry in (fourthConjDep):
        strippedEntry = [x.strip() for x in entry.split(',')];
        firstPP = strippedEntry[0];
        secondPP = strippedEntry[1];
        presStem = secondPP[:-3];
        createQuestion("Gerundive of " + firstPP, "Produce the masculine nominative singular gerundive of " + entry, getAnswers(secondPP[:-3] + "iendus"), []);

#Creates a set of questions under a single category name (change below)
#Call one or more "create" functions here to populate the XML file with questions.
def createQuiz():
    global outText;
    global indentLevel;
    addIndents();
    outText += "<quiz>\n";
    indentLevel = indentLevel + 1;
    #createCategory("Test Nouns");
    createCategory("Gerundives");
    createGerundiveQuestions();
    createDeponentGerundiveQuestions();
    #createFirstDeclQuestions();
    #createSecondDeclMQuestions();
    #createSecondDeclNQuestions();
    #createThirdDeclConsMFQuestions();
    #createThirdDeclConsNQuestions();
    #createThirdDeclIMFQuestions();
    #createThirdDeclINQuestions();
    #createFourthDeclMFQuestions();
    #createFourthDeclNQuestions();
    #createFifthDeclQuestions();
    #createQuestion("Test Question", "Produce the nominative plural of agricola", ["agricolae"], []);
    #createQuestion("Test Question 2", "Produce the genitive plural of agricola", ["agricolarum", "agricolārum"], []);
    indentLevel = indentLevel - 1;
    addIndents();
    outText += "</quiz>"
    return;

#Create a set of questions and write to the output file, creating if it doesn't exist and overwriting it if it does.
#Sets the encoding properly to allow macrons in output.
createQuiz();
f1=open(outFile, 'w+', encoding='utf-8');
f1.write(outText);
f1.close();
