function formChange() {

    var subjects = document.fmSubjects.slSubjects;
    var selectedIndex = subjects.selectedIndex;
    var optionText = subjects.options[selectedIndex].text;

    if(selectedIndex != 0 ) {

        var account = "welt2000";
        var domain  = "gmx.net";

        var recipient = account + "@" + domain;
        var subject   = "[" + optionText + "] ";

        document.getElementById("maillink").href =
            "mailto:"  + recipient + "?" +
            "subject=" + subject;

        document.getElementById("message").style.visibility = "hidden";
    }
    else {
        document.getElementById("maillink").href = document.location.href;
        document.getElementById("message").style.visibility = "visible";
    }
}
