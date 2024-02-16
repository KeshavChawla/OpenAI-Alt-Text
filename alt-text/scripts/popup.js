$( document ).ready(function() {
    chrome.storage.local.get(["apiKey"]).then((result) => {
        $("#apiKey").val(result.apiKey);
    });
});

$("#saveApiKey").click(function () {
    chrome.storage.local.set({ "apiKey": $("#apiKey").val() }, function(){
        // API key set
    });
});