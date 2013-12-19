var baseURL = "http://www.segelflug.de/vereine/welt2000/content/";

var subjects = new Array();
subjects['de'] = "Beitrag";
subjects['en'] = "Contribution";

var myContrib = new Array();
myContrib['de'] = "Mein Beitrag";
myContrib['en'] = "My contribution";

var acceptContribTerms = new Array();
acceptContribTerms['de'] = "Ich akzeptiere die Bestimmungen fuer Mitwirkende\n--> " + baseURL + "de/legal/contributor-terms.php";
acceptContribTerms['en'] = "I accept the Contribution Terms\n--> " + baseURL + "en/legal/contributor-terms.php";

var acceptPrivPolicy = new Array();
acceptPrivPolicy['de'] = "Ich akzeptiere die Datenschutz-Bestimmungen\n--> " + baseURL + "de/legal/privacy-policy.php";
acceptPrivPolicy['en'] = "I accept the Privacy Policy\n--> " + baseURL + "en/legal/privacy-policy.php";

function formChange(language) {

    var account = "welt2000";
    var domain  = "gmx.net";

    recipient = account + "@" + domain;

    if (document.fmChecks.cbContribTerms.checked == true && document.fmChecks.cbPrivPolicy.checked == true) {

        subject   = "[" + subjects[language] + "] ";
        body      = escape(myContrib[language]) + ":%0D%0A%0D%0A%0D%0A%0D%0A"
                    + escape(acceptContribTerms[language]) + "%0D%0A"
                    + escape(acceptPrivPolicy[language])   + "%0D%0A";

        document.getElementById("maillink").href =
            "mailto:"  + recipient + "?" +
            "subject=" + subject + "&" +
            "body="    + body;

        document.getElementById("message").style.visibility = "hidden";
    }
    else {
        document.getElementById("maillink").href = "data.php";
        document.getElementById("message").style.visibility = "visible";
    }
}
