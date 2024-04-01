$( document ).ready(function() {
    chrome.storage.local.get(["apiKey"]).then((result) => {
        $("#apiKey").val(result.apiKey);
    });
    
    chrome.storage.local.get(["overwriteAltTags"]).then((result) => {
        $("#overwriteAltTags").prop("checked", result.overwriteAltTags);
    });
    
    chrome.storage.local.get(["includeColorDescription"]).then((result) => {
        $("#includeColorDescription").prop("checked",result.includeColorDescription);
    });
    
    chrome.storage.local.get(["extraDetailedDescription"]).then((result) => {
        $("#extraDetailedDescription").prop("checked",result.extraDetailedDescription);
    });
});

$("#saveApiKey").click(function () {
    chrome.storage.local.set({ "apiKey": $("#apiKey").val() }, function(){
        // API key set
        $("#saveApiKey").html("Saved key!");
        $("#saveApiKey").prop("disabled", true);
    });
});

$('#overwriteAltTags').change(function() {
    console.log(this.checked);
    chrome.storage.local.set({ "overwriteAltTags": this.checked }, function(){
        // overwriteAltTags set
    });
});

$('#includeColorDescription').change(function() {
    console.log(this.checked);
    chrome.storage.local.set({ "includeColorDescription": this.checked }, function(){
        // includeColorDescription set
    });
});

$('#extraDetailedDescription').change(function() {
    console.log(this.checked);
    chrome.storage.local.set({ "extraDetailedDescription": this.checked }, function(){
        // extraDetailedDescription set
    });
});