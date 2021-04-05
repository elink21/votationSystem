
const clearSelections = () => {
    let scientific = document.querySelector("#scientific");
    let workers = document.querySelector("#worker");
    let democrat = document.querySelector("#democrat");

    let options = [scientific, workers, democrat];

    for (option of options) {
        option.classList.remove("selected");
    }
}


const selectParty = (partyID,revote) => {
    if(revote)vote(partyID);
    console.log("here");
    clearSelections();
    let selected = document.querySelector("#" + partyID);
    selected.classList.add("selected");
}

const vote = (party) => {
    $.ajax({
        url: 'saveVote',
        data: { 'party': party },
        success: () => {
            M.toast({ html: "Vote registered ✅" });
        }
    })
}


window.onload = () => {
    selectParty(actualVote,false);
}

