function applyFilters() {
    let typeValue = document.getElementById("type-field").value ? document.getElementById("type-field").value : null;
    let gameValue = document.getElementById("game-field").value ? document.getElementById("game-field").value : null;
    let orderByValue = document.getElementById("orderby-field").value ? document.getElementById("orderby-field").value : null;

    link = window.location.href.split('?')[0];
    link = `${link}?`
    if (typeValue) { link += `type=${typeValue}&` }
    if (gameValue) { link += `game=${gameValue}&` }
    if (orderByValue) { link += `orderby=${orderByValue}&` }

    window.location.href = link;
}