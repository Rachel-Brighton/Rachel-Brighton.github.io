import os
import sys

def generateHTML(codes):
	output_html_file = "search.html"

	# Start creating the HTML file content
	html_content = '''<html>
<head>
  <title>Search</title>
  <link rel="icon" type="image/x-icon" href="/img/search.png">
  <link rel="stylesheet" href="resources/mana.css">
  <link rel="stylesheet" href="/resources/header.css">
</head>
<style>
	body {
		font-family: 'Helvetica', 'Arial', sans-serif;
		overscroll-behavior: none;
		margin: 0px;
		background-color: #f3f3f3;
	}
	.button-grid {
		width: 70%;
		max-width: 1200px;
		height: 40px;
		margin: auto;
		display: grid;
		grid-template-columns: 4fr 1fr;
		gap: 10px;
		padding-top: 20px;
		padding-bottom: 20px;
		justify-items: center;
	}
	.prev-next-btns {
		width: 100%;
		height: 40px;
		margin: auto;
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 5px;
	}
	button {
	  background-color: #fafafa;
	  border: 1px solid #d5d9d9;
	  border-radius: 8px;
	  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;
	  color: #171717;
	  cursor: pointer;
	  font-size: 13px;
	  width: 100%;
	  height: 35px;
	  min-width: 85px;
	}
	button:hover {
	  background-color: #ffffff;
	}
	button:focus {
	  border-color: #171717;
	  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;
	  outline: 0;
	}
	button:disabled {
		cursor: auto;
		background-color: #f7fafa;
		font-style: italic;
		box-shadow: none;
		color: #cccccc;
	}
	.button-grid .results-text {
		margin-right: -3px;
	}
	.button-grid .select-text {
		width: 100%;
		display: flex;
		align-items: center;
		justify-content: left;
		gap: 8px;
		font-size: 14.5px;
	}
	select {
		background-color: #fafafa;
	  border: 1px solid #d5d9d9;
	  border-radius: 8px;
	  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;
		text-align: center;
	  color: #171717;
	  font-size: 13px;
	  height: 30px;
	}
	.grid-container {
		display: grid;
		grid-template-columns: auto;
		max-width: 1200px;
		margin: auto;
	}
	.image-grid-container {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr 1fr;
		width: 70%;
		max-width: 1200px;
		margin: auto;
		gap: 5px;
		justify-items: center;
	}
	@media ( max-width: 750px ) {
	  .image-grid-container {
			grid-template-columns: 1fr 1fr;  
		}
	}
	.image-grid {
		width: 70%;
		margin: auto;
		display: grid;
		grid-template-columns: minmax(150px, 1fr) minmax(300px, 2fr);
		gap: 50px;
		padding-bottom: 10px;
		justify-items: left;
	}
	.image-grid img {
		position: relative;
	}
	.card-image {
		float: left;
		width: 100%;
		height: auto;
		display: block;
	}
	.card-text {
		padding-top: 20px;
		padding-bottom: 20px;
		background: #fcfcfc;
		width: 100%;
		border: 1px solid #d5d9d9;
		border-top: 3px solid #171717;
		border-bottom: 3px solid #171717;
		border-radius: 6px;
		height: fit-content;
		min-height: 75%;
		margin-top: 3%;
	}
	.card-text div {
		white-space: normal;
		font-size: 15px;
		padding-bottom: 10px;
		padding-left: 12px;
		padding-right: 12px;
		line-height: 155%;
	}
	.card-text .name-cost {
		font-weight: bold;
		font-size: 20px;
		white-space: pre-wrap;
	}
	.card-text .type {
		font-size: 16px;
	}
	.card-text .pt {
		font-weight: bold;
	}
	.card-text br {
		content: "";
		display: block;
		margin-bottom: 5px;
	}
	.img-container {
	  position: relative;
	  width: 100%;
	  align-self: center;
	}
	.img-container img {
	  width: 100%;
	  height: auto;
	}
	.img-container .btn {
		background: url('img/flip.png') no-repeat;
		background-size: contain;
		background-position: center;
		width: 15%;
		height: 11%;
		cursor: pointer;
		border: none;
		position: absolute;
		top: 6.5%;
		left: 8.5%;
		transform: translate(-50%, -85%);
	}
	.img-container .btn:hover {
		background: url('img/flip-hover.png') no-repeat;
		background-size: contain;
		background-position: center;
		width: 15%;
		height: 11%;
		cursor: pointer;
		border: none;
		position: absolute;
		top: 6.5%;
		left: 8.5%;
		transform: translate(-50%, -85%);
	}
</style>
<body>
	<div class="header">
		<div class="search-grid">
			<a href="/"><img class="sg-logo" src="/img/banner.png"></a>
			<img class="sg-icon" src="/img/search.png">
			<input type="text" inputmode="search" placeholder="Search ..." name="search" id="search" spellcheck="false" autocomplete="off" autocorrect="off" spellcheck="false">
			<a href="/all-sets"><img src="/img/sets.png" class="sg-icon">Sets</a>
			<a onclick="randomCard()"><img src="/img/random.png" class="sg-icon">Random</a>
		</div>
	</div>
	<div class="button-grid">
		<div class="select-text"><div class="results-text" id="results-text">Loading ...</div>Cards displayed as<select name="display" id="display"><option value="cards-only">Cards Only</option><option value="cards-text">Cards + Text</option></select>sorted by<select name="sort-by" id="sort-by"><option value="name">Name</option><option value="set-code">Set / Number</option><option value="mv">Mana Value</option><option value="color">Color</option></select></div>		
		<div class="prev-next-btns">
			<button type="submit" onclick="previousPage()" id="prevBtn" disabled>< Previous</button>
			<button type="submit" onclick="nextPage()" id="nextBtn">Next 30 ></button>
		</div>
	</div>

	<div class="grid-container" id="grid">
	</div>

	<div class="image-grid-container" id="imagesOnlyGrid">
	</div>

	<div class="button-grid" id="footer">
		<div></div>
		<div class="prev-next-btns">
			<button type="submit" onclick="previousPage()" id="prevBtn-footer" disabled>< Previous</button>
			<button type="submit" onclick="nextPage()" id="nextBtn-footer">Next 30 ></button>
		</div>
	</div>

	<script>
		let page = 0;
		let pageCount = 30;
		let search_results = [];
		let card_list_arrayified = [];
		let specialchars = "";

		document.addEventListener("DOMContentLoaded", async function () {
			await fetch('./lists/all-cards.txt')
				.then(response => response.text())
				.then(text => {
					card_list_stringified = text; 
			}).catch(error => console.error('Error:', error));

			await fetch('/resources/replacechars.txt')
				.then(response => response.text())
				.then(text => {
					specialchars = text; 
			}).catch(error => console.error('Error:', error));

			card_list_arrayified = card_list_stringified.split('\\\\n');

			for (let i = 0; i < card_list_arrayified.length; i++)
			{
				card_list_arrayified[i] = card_list_arrayified[i].split('\t');
			}

			if (sessionStorage.getItem("display") != "cards-only")
			{
				cardGrid = document.getElementById("grid");
			}
			else
			{
				cardGrid = document.getElementById("imagesOnlyGrid");
			}

			card_list_arrayified.sort(compareFunction);

			page = window.location.href.indexOf("page=") == -1 ? 0 : parseInt(window.location.href.substring(window.location.href.indexOf("page=") + 5)) - 1;

			// refresh page values
			let params = decodeURIComponent(window.location.href.indexOf("?search") == -1 ? "" : window.location.href.substring(window.location.href.indexOf("?search") + 8));
  			document.getElementById("search").value = (params.indexOf("&page=") == -1 ? params.replaceAll("+", " ") : params.substring(0, params.indexOf("&page=")).replaceAll("+", " "));
  			if (sessionStorage.getItem("sortMethod"))
  			{
	  			document.getElementById("sort-by").value = sessionStorage.getItem("sortMethod");  			
  			}
  			if (sessionStorage.getItem("display"))
  			{
	  			document.getElementById("display").value = sessionStorage.getItem("display");  			
  			}

  			displayStyle = document.getElementById("display").value;
  			setCardView();

  			// initial search on load
			preSearch(false);
		});

		document.getElementById("sort-by").onchange = sortChangeListener;
  
  		function sortChangeListener() {
  			sessionStorage.setItem("sortMethod", document.getElementById("sort-by").value);
  			preSearch(false);
  		}

  		document.getElementById("display").onchange = displayChangeListener;
  
  		function displayChangeListener() {
  			displayStyle = document.getElementById("display").value;
  			sessionStorage.setItem("display", displayStyle);

  			setCardView();

  			preSearch(false);
  		}

  		window.addEventListener('popstate', function(event) {
  			let params = decodeURIComponent(window.location.href.indexOf("?search") == -1 ? "" : window.location.href.substring(window.location.href.indexOf("?search") + 8), (window.location.href.indexOf("page=") == -1 ? window.location.href.length : window.location.href.indexOf("page=")));
			document.getElementById("search").value = (params.indexOf("&page=") == -1 ? params.replaceAll("+", " ") : params.substring(0, params.indexOf("&page=")).replaceAll("+", " "));
			page = window.location.href.indexOf("page=") == -1 ? 0 : parseInt(window.location.href.substring(window.location.href.indexOf("page=") + 5)) - 1;

			preSearch(false);
		});

		function setCardView() {
			imagesOnlyGrid.style.display = displayStyle == "cards-only" ? '' : 'none';
  		grid.style.display = displayStyle == "cards-only" ? 'none' : '';
		}

		function compareFunction(a, b) {
			const sortMode = document.getElementById("sort-by").value;
			
			if (sortMode == 'set-code')
			{
				if (a[11] === b[11])
				{
					if (a[4] === b[4])
					{
						return 0;
					}
					else {
						return (parseInt(a[4]) < parseInt(b[4])) ? -1 : 1;
					}
				}
				else {
					return (a[11] < b[11]) ? -1 : 1;
				}
			}
			if (sortMode == 'name')
			{
				if (a[0] === b[0])
				{
					return 0;
				}
				else {
					return (a[0] < b[0]) ? -1 : 1;
				}
			}
			if (sortMode == 'mv')
			{
				a_mv = isDecimal(a[6].charAt(0)) ? parseInt(a[6]) + a[6].replaceAll('x','').length - 1 : a[6].replaceAll('x','').length;
				b_mv = isDecimal(b[6].charAt(0)) ? parseInt(b[6]) + b[6].replaceAll('x','').length - 1 : b[6].replaceAll('x','').length;
				if (a_mv === b_mv)
				{
					if (a[0] === b[0])
					{
						return 0;
					}
					else {
						return (a[0] < b[0]) ? -1 : 1;
					}
				}
				else {
					return (a_mv < b_mv) ? -1 : 1;
				}
			}
			if (sortMode == 'color')
			{
				color_sort_order = ["W", "U", "B", "R", "G", "WU", "UB", "BR", "RG", "GW", "WB", "UR", "BG", "RW", "GU", "WUB", "UBR", "BRG", "RGW", "GWU", "RWB", "GUR", "WBG", "URW", "BGU", "WUBR", "UBRG", "BRGW", "RGWU", "GWUB", "WUBRG", ""];
				a_color_index = -1;
				b_color_index = -1;

				for (let i = 0; i < color_sort_order.length; i++)
				{
					if (a[1].toLowerCase().split('').sort().join('') == color_sort_order[i].toLowerCase().split('').sort().join(''))
					{
						a_color_index = i;
					}
					if (b[1].toLowerCase().split('').sort().join('') == color_sort_order[i].toLowerCase().split('').sort().join(''))
					{
						b_color_index = i;
					}
				}

				if (a_color_index === b_color_index)
				{
					if (a[0] === b[0])
					{
						return 0;
					}
					else {
						return (a[0] < b[0]) ? -1 : 1;
					}
				}
				else {
					return (a_color_index < b_color_index) ? -1 : 1;
				}
			}
		}

		function preSearch(setNewState) {
			card_list_arrayified.sort(compareFunction);
			search_results = [];
			page = setNewState ? 0 : page;

			search(setNewState);
		}

		function search(setNewState) {
			searchTerms = document.getElementById("search").value.toLowerCase();

			if (searchTerms != "")
			{
				if (setNewState)
				{
					let url = (window.location.href.indexOf("?") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("?"))));
					let params = new URLSearchParams(url.search);
					params.append("search", searchTerms);
					history.pushState({}, '', url.pathname + '?' + params.toString());
				}
			}
			else
			{
				if (setNewState)
				{
					let url = (window.location.href.indexOf("?") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("?"))));
					let params = new URLSearchParams(url.search);
					params.delete("search");
					history.pushState({}, '', url.pathname + '' + params.toString());
				}
			}

			if (displayStyle == "cards-only")
			{
				cardGrid = document.getElementById("imagesOnlyGrid");
			}
			else
			{
				cardGrid = document.getElementById("grid");
			}
			cardGrid.innerHTML = "";

			for (const card of card_list_arrayified) {
				if (card[3].includes("Token") && !searchTerms.includes("*t:token") && !searchTerms.includes("t:token"))
				{
					continue;
				}

				if (card[3].includes("Basic") && !searchTerms.includes("*t:basic") && !searchTerms.includes("t:basic"))
				{
					continue;
				}

				searched = searchAllTokens(card, tokenizeTerms(searchTerms));

				if (searched)
				{
					search_results.push(card);
				}
			}

			if (searchTerms != "")
			{
				document.getElementById("results-text").innerText = search_results.length + (search_results.length == 1 ? " result found." : " results found.");
			}
			else
			{
				document.getElementById("results-text").innerText = "";
			}

			if (page != 0)
			{
				document.getElementById("prevBtn").disabled = false;
				document.getElementById("prevBtn-footer").disabled = false;
			}
			else
			{
				document.getElementById("prevBtn").disabled = true;
				document.getElementById("prevBtn-footer").disabled = true;
			}

			// set text of Next to match number of displayed images
			displayStyle = document.getElementById("display").value;
  			pageCount = displayStyle == "cards-only" ? 60 : 30;
  			document.getElementById("nextBtn").innerText = "Next " + pageCount + " >";
  			document.getElementById("nextBtn-footer").innerText = "Next " + pageCount + " >";

  			// really awesome code block to fix the URL when switching from Cards + Text view to Cards Only view
  			while ((pageCount * page) > search_results.length)
  			{
  				page = page - 1;

  				let url = (window.location.href.indexOf("page=") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("page="))));
				let params = new URLSearchParams(url.search);
				params.append("page", page+1);
				history.replaceState({}, '', url.pathname + '?' + params.toString());
  			}

			for (let i = (pageCount * page); i < Math.min((pageCount * (page + 1)), search_results.length); i++)
			{
				cardGrid.appendChild(gridifyCard(search_results[i]));
			}

			if (search_results.length <= (pageCount * (page + 1)))
			{
				document.getElementById("nextBtn").disabled = true;
				document.getElementById("nextBtn-footer").disabled = true;
			}
			else
			{
				document.getElementById("nextBtn").disabled = false;
				document.getElementById("nextBtn-footer").disabled = false;
			}
		}

		function tokenizeTerms(searchTerms)
		{
			let searchTokens = [];
			let key = 0;
			let inParens = false;
			let inQuotes = false;
			for (let i = 0; i < searchTerms.length; i++)
			{
				if (searchTerms.charAt(i) == '(')
				{
					inParens = true;
				}
				if (searchTerms.charAt(i) == ')')
				{
					inParens = false;
				}
				if (!inParens && !inQuotes && (searchTerms.charAt(i) == '"' || searchTerms.charAt(i) == '“' || searchTerms.charAt(i) == '/'))
				{
					inQuotes = true;
				}
				else if (!inParens && inQuotes && (searchTerms.charAt(i) == '"' || searchTerms.charAt(i) == '”' || searchTerms.charAt(i) == '/'))
				{
					inQuotes = false;
				}
				if (searchTerms.charAt(i) == ' ' && !inParens && !inQuotes)
				{
					searchTokens.push(searchTerms.substring(key, i));
					key = i + 1;
				}
				if (i == searchTerms.length - 1)
				{
					searchTokens.push(searchTerms.substring(key));
				}
			}

			return searchTokens;
		}

		function searchAllTokens(card, tokens)
		{
			if (tokens.length < 1)
			{
				return true;
			}
			for (let i = 0; i < tokens.length; i++)
			{
				if (tokens[i].charAt(0) == '*')
				{
					return searchAllTokens(card, tokens.slice(0, i)) && searchAllTokens(card, tokens.slice(i + 1));
				}
				if (tokens[i] == "or")
				{
					return searchAllTokens(card, tokens.slice(0, i)) || searchAllTokens(card, tokens.slice(i + 1));
				}
			}

			for (let token of tokens)
			{
				if (token.charAt(0) == '-')
				{
					return !searchToken(card, token.substring(1)) && (tokens.length == 1 ? true : searchAllTokens(card, tokens.slice(1)));
				}
				if (token.charAt(0) == '(')
				{
					return searchAllTokens(card, tokenizeTerms(token.substring(1, token.length - 1))) && (tokens.length == 1 ? true : searchAllTokens(card, tokens.slice(1)));
				}
				else
				{
					return searchToken(card, token) && (tokens.length == 1 ? true : searchAllTokens(card, tokens.slice(1)));
				}
			}
		}

		function searchToken(card, token)
		{
			let card_stats = [];

			for (let i = 0; i < card.length; i++)
			{
				card_stats.push(card[i].toLowerCase());
			}

			let card_name = card_stats[0];
			let card_color = card_stats[1] != "" ? card_stats[1] : "c";
			let card_rarity = card_stats[2];
			let card_type = card_stats[3];
			// 4: collector number
			let card_ci = card_stats[5];
			let card_mv = isDecimal(card_stats[6].charAt(0)) ? parseInt(card_stats[6]) + card_stats[6].replaceAll('x','').length - 1 : card_stats[6].replaceAll('x','').length;
			let card_oracle_text = card_stats[7] != "" ? card_stats[7].replaceAll("NEWLINE", '\\n') : card_stats[9].replaceAll("NEWLINE", '\\n');
			let card_power = card_stats[8].substring(0,card_stats[8].indexOf('/'));
			let card_toughness = card_stats[8].substring(card_stats[8].indexOf('/')+1);
			let card_shape = card_stats[10];
			let card_set = card_stats[11];

			// two cards in one	
			if (card_shape.includes("adventure") || card_shape.includes("double") || card_shape.includes("spli"))
			{
				card_name = card_name + "	" + card_stats[12];
				card_type = card_type + "	" + card_stats[14];
				card_oracle_text = card_oracle_text + "	" + (card_stats[17] != "" ? card_stats[17].replaceAll("NEWLINE", '\\n') : card_stats[19].replaceAll("NEWLINE", '\\n'));
			}

			token = token.replaceAll("~", card_name).replaceAll("cardname", card_name).replaceAll('"','').replaceAll('/','').replaceAll('“','').replaceAll('”','');

			const modifierRegex = /[!:<>=]/;
			const match = token.search(modifierRegex);

			if (match > -1)
			{
				const term = token.substring(0, match);
				const modifier = token.charAt(match);
				const check = token.substring(match + 1);

				// availableTokens = ["mv", "c", "ci", "t", "o", "pow", "tou", "r", "is"]

				/* template
				if (term == "mv")
				{
					if (modifier == "!" || modifier == "=")
					{

					}
					else if (modifier == ":")
					{

					}
					else if (modifier == "<")
					{

					}
					else if (modifier == ">")
					{

					}
				} */
				if (term == "mv")
				{
					if (modifier == "!" || modifier == "=")
					{
						return (card_mv == check);
					}
					else if (modifier == ":")
					{
						return (card_mv == check);
					}
					else if (modifier == "<")
					{
						return (card_mv < check);
					}
					else if (modifier == ">")
					{
						return (card_mv > check);
					}
				}
				if (term == "c")
				{
					if (modifier == "!" || modifier == "=")
					{
						if (!isNaN(check))
						{
							return card_color.length == parseInt(check);
						}
						return (card_color.split("").sort().join("") == check.split("").sort().join(""));
					}
					else if (modifier == ":")
					{
						if (!isNaN(check))
						{
							return card_color.length == parseInt(check);
						}
						return hasAllChars(card_color, check);
					}
					else if (modifier == "<")
					{
						if (!isNaN(check))
						{
							return card_color.length < parseInt(check);
						}
						return hasNoChars(card_color, check);
					}
					else if (modifier == ">")
					{
						if (!isNaN(check))
						{
							return card_color.length > parseInt(check);
						}
						return hasAllAndMoreChars(card_color, check);
					}
				}
				if (term == "ci")
				{
					if (modifier == "!" || modifier == "=")
					{
						// why is this the best way to do this?
						if (!isNaN(check))
						{
							return card_ci.length == parseInt(check);
						}
						return (card_ci.split("").sort().join("") == check.split("").sort().join(""));
					}
					else if (modifier == ":")
					{
						if (!isNaN(check))
						{
							return card_ci.length == parseInt(check);
						}
						return hasAllChars(card_ci, check);
					}
					else if (modifier == "<")
					{
						if (!isNaN(check))
						{
							return card_ci.length < parseInt(check);
						}
						return hasNoChars(card_ci, check);
					}
					else if (modifier == ">")
					{

						if (!isNaN(check))
						{
							return card_ci.length > parseInt(check);
						}
						return hasAllAndMoreChars(card_ci, check);
					}
				}
				if (term == "t" || term == "type")
				{
					if (modifier == ":")
					{
						return card_type.includes(check);
					}
					/* unsupported flows
					if (modifier == "!" || modifier == "=")
					{

					}
					else if (modifier == "<")
					{

					}
					else if (modifier == ">")
					{

					} */
				}
				if (term == "o")
				{
					if (modifier == ":")
					{
						regex = new RegExp(check);
						return regex.test(card_oracle_text);
						if (check.charAt(0) == '/')
						{
							
							return regex.test(card_oracle_text);
						}
						else
						{
							return card_oracle_text.includes(check);
						}
					}
					/* unsupported flows
					if (modifier == "!" || modifier == "=")
					{

					}
					else if (modifier == "<")
					{

					}
					else if (modifier == ">")
					{

					} */
				}
				if (term == "pow")
				{
					if (modifier == "!" || modifier == "=")
					{
						return (card_power == check);
					}
					else if (modifier == ":")
					{
						return (card_power == check);
					}
					else if (modifier == "<")
					{
						return (card_power < check);
					}
					else if (modifier == ">")
					{
						return (card_power > check);
					}
				}
				if (term == "tou")
				{
					if (modifier == "!" || modifier == "=")
					{
						return (card_toughness == check);
					}
					else if (modifier == ":")
					{
						return (card_toughness == check);
					}
					else if (modifier == "<")
					{
						return (card_toughness < check);
					}
					else if (modifier == ">")
					{
						return (card_toughness > check);
					}
				}
				if (term == "r")
				{
					if (modifier == ":")
					{
						return (card_rarity == check);
					}
					/* unsupported flows
					if (modifier == "!" || modifier == "=")
					{

					}
					else if (modifier == "<")
					{

					}
					else if (modifier == ">")
					{

					} */
				}
				if (term == "e")
				{
					if (modifier == ":")
					{
						return (card_set == check);
					}
					/* unsupported flows
					if (modifier == "!" || modifier == "=")
					{

					}
					else if (modifier == "<")
					{

					}
					else if (modifier == ">")
					{

					} */
				}
				if (term == "is")
				{
					if (modifier == ":")
					{
						// all of these are implemented individually
						if (check == "permanent")
						{
							return !card_type.includes("instant") && !card_type.includes("sorcery");
						}
						if (check == "spell")
						{
							return !card_type.includes("land");
						}
						if (check == "commander")
						{
							return (card_type.includes("legendary") && card_type.includes("creature")) || card_oracle_text.includes("can be your commander");
						}
					}
					/* unsupported flows
					if (modifier == "!" || modifier == "=")
					{

					}
					else if (modifier == "<")
					{

					}
					else if (modifier == ">")
					{

					} */
				}
			}

			return card_name.includes(token);
		}

		function isDecimal(char) {
			return char >= '0' && char <= '9';
		}

		function tokenize(text) {
			let tokens = [];

			for (let i = 0; i < text.length; i++)
			{
				if (i < text.length - 1)
				{
					if (text[i + 1] == '/')
					{
						tokens.push(text.substring(i, i + 3));
						i = i + 2;
					}
					else if (isDecimal(text[i]) && isDecimal(text[i + 1]))
					{
						tokens.push(text.substring(i, i + 2));
						i = i + 1;
					}
					else
					{
						tokens.push(text[i]);
					}
				}
				else
				{
					tokens.push(text[i]);
				}
			}

			return tokens;
		}

		function symbolize(text) {
			let tokens = tokenize(text);
			let symText = "";
			for (const token of tokens)
			{
				symText = symText + "{" + token + "}";
			}

			return formatTextHTML(symText);
		}

		function formatTextHTML(str) {
			if(!str)
				return "";
			str = str.replace(/[{]([^}]+)[}]/g, function(matched, _1) {
				let letters = _1.toLowerCase().replace("/", "")
				return '<span class="mana mana-cost mana-' + letters + '"></span>';
			})
			return str;
		}

		function gridifyCard(card_stats) {
			const card_name = card_stats[0];

			if (displayStyle == "cards-only")
			{
				return buildImgContainer(card_stats);
			}

			const grid = document.createElement("div");
			grid.className = "image-grid";

			grid.appendChild(buildImgContainer(card_stats));
			
			const text = document.createElement("div");
			text.className = "card-text";

			const name_cost = document.createElement("div");
			name_cost.className = "name-cost";
			name_cost.innerHTML = card_stats[0] + (card_stats[6] != "" ? '     ' + symbolize(card_stats[6]) : "");
			text.appendChild(name_cost);

			const type = document.createElement("div");
			type.className = "type";
			type.textContent = card_stats[3];
			text.appendChild(type);

			const effect = document.createElement("div");
			effect.className = "effect";
			let card_effects = "";
			if (card_stats[7] != "")
			{
				card_effects = card_stats[7].split("NEWLINE");
			}
			else
			{
				card_effects = card_stats[9].split("NEWLINE");
			}
			effect.innerHTML += prettifyEffects(card_effects);
			text.appendChild(effect);

			if(card_stats[8] != "")
			{
				const pt = document.createElement("div");
				pt.className = "pt";
				pt.textContent = card_stats[8];
				text.appendChild(pt);
			}

			// 12-name	13-color	14-type	15-ci	16-cost	17-ability	18-pt	19-special-text	
			if(card_stats[10].includes("adventure") || card_stats[10].includes("double") || card_stats[10].includes("spli"))
			{
				const name_cost_2 = document.createElement("div");
				name_cost_2.className = "name-cost";
				name_cost_2.innerHTML = card_stats[12] + (card_stats[16] != "" ? '     ' + symbolize(card_stats[16]) : "");
				text.appendChild(name_cost_2);

				const type_2 = document.createElement("div");
				type_2.className = "type";
				type_2.textContent = card_stats[14];
				text.appendChild(type_2);

				const effect_2 = document.createElement("div");
				effect_2.className = "effect";
				let card_effects_2 = "";
				if (card_stats[17] != "")
				{
					card_effects_2 = card_stats[17].split("NEWLINE");
				}
				else
				{
					card_effects_2 = card_stats[19].split("NEWLINE");
				}
				effect_2.innerHTML += prettifyEffects(card_effects_2);
				text.appendChild(effect_2);

				if(card_stats[18] != "")
				{
					const pt_2 = document.createElement("div");
					pt_2.className = "pt";
					pt_2.textContent = card_stats[18];
					text.appendChild(pt_2);
				}
			}
			
			grid.appendChild(text);

			return grid;
		}

		function buildImgContainer(card_stats) {
			const imgContainer = document.createElement("div");
			imgContainer.className = "img-container";
			const id = card_stats[11] + "-" + card_stats[4] + "-" + document.getElementById("display").value;

			const img = document.createElement("img");
			img.className = "card-image";
			img.id = id;
			// (card_stats[12].includes("_") ? card_stats[12] : card_stats[0]) for posterity
			img.src = "/sets/" + card_stats[11] + "-files/img/" + card_stats[4] + (card_stats[3].includes("Token") ? "t_" : "_") + card_stats[0] + ((card_stats[10].includes("double")) ? "_front" : "") + ".png";
			
			const link = document.createElement("a");
			let card_name = card_stats[0];
			for (const char of specialchars)
			{
				card_name = card_name.replaceAll(char, "");
			}
			link.href = "/cards/" + card_stats[11] + "/" + card_stats[4] + "_" + card_name;
			link.appendChild(img);
			imgContainer.appendChild(link);

			if (card_stats[10].includes("double"))
			{
				const imgFlipBtn = document.createElement("button");
				imgFlipBtn.className = "btn";
				imgFlipBtn.onclick = function() { imgFlip(id); };
				imgContainer.appendChild(imgFlipBtn);
			}

			return imgContainer;
		}

		function imgFlip(id) {
			cardToFlip = document.getElementById(id);
			cardName = cardToFlip.src;
			
			cardToFlip.src = cardName.includes("_front") ? cardName.replace("_front", "_back") : cardName.replace("_back", "_front");
		}

		function prettifyEffects(card_effects) {
			let HTML = "";

			for (let i = 0; i < card_effects.length; i++)
			{
				let styled_effect = card_effects[i].replaceAll("(","<i>(").replaceAll(")",")</i>");

				if (styled_effect.includes("—") && !styled_effect.toLowerCase().includes("choose"))
				{
					styled_effect = "<i>" + styled_effect.replace("—", "—</i>");
				}

				HTML += styled_effect;

				if (i != card_effects.length - 1)
				{
					HTML += "<br>"
				}
			}

			let pattern1 = /([0-9X]*[WUBRGCT/]+)([ :,\.])/g;
			let pattern2 = /(?<![a-z] |\/[0-9X]*)([0-9X]+)([:,])/g;
			let pattern3 = /([Pp]ay[s]* |[Cc]ost[s]* |[Ww]ard )([0-9X])(?! life)/g;
			let pattern5 = /(Equip [^(<]*)([0-9XWUBRGC/]+)/g;
			let regexHTML = HTML.replace(pattern1, function (match, group1, group2) {
				return symbolize(group1) + group2;
			});
			regexHTML = regexHTML.replace(pattern2, function (match, group1, group2) {
				return symbolize(group1) + group2;
			});
			regexHTML = regexHTML.replace(pattern3, function (match, group1, group2) {
				return group1 + symbolize(group2);
			});
			regexHTML = regexHTML.replace(pattern5, function (match, group1, group2) {
				return group1 + symbolize(group2);
			});

			return regexHTML;
		}

		function hasAllChars(strOut, strIn) {
			let retVal = true;

			for (let i = 0; i < strIn.length; i++)
			{
				if (!strOut.includes(strIn.charAt(i)))
				{
					retVal = false;
				}
			}

			return retVal;
		}

		function hasNoChars(strOut, strIn) {
			let retVal = true;

			for (let i = 0; i < strIn.length; i++)
			{
				if (strOut.includes(strIn.charAt(i)))
				{
					retVal = false;
				}
			}

			return retVal;
		}

		function hasAllAndMoreChars(strOut, strIn) {
			let retVal = true;

			for (let i = 0; i < strIn.length; i++)
			{
				if (!strOut.includes(strIn.charAt(i)))
				{
					retVal = false;
				}
			}

			return retVal && (strOut.length > strIn.length);
		}

		document.getElementById("search").addEventListener("keypress", function(event) {
		  if (event.key === "Enter") {
			event.preventDefault();
			preSearch(true);
		  }
		});

		function previousPage() {
			page = page - 1;
			cardGrid.innerHTML = "";

			let url = (window.location.href.indexOf("page=") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("page="))));
			let params = new URLSearchParams(url.search);
			if (page != 0)
			{
				params.append("page", page+1);
			}
			history.pushState({}, '', url.pathname + '?' + params.toString());

			for (let i = (pageCount * page); i < Math.min((pageCount * (page + 1)), search_results.length); i++)
			{
				cardGrid.appendChild(gridifyCard(search_results[i]));
			}

			document.getElementById("nextBtn").disabled = false;
			document.getElementById("nextBtn-footer").disabled = false;
			if (page == 0)
			{
				document.getElementById("prevBtn").disabled = true;
				document.getElementById("prevBtn-footer").disabled = true;
			}

			document.body.scrollTop = 0; // For Safari
  			document.documentElement.scrollTop = 0; // For real browsers
		}

		function nextPage() {
			page = page + 1;
			
			let url = (window.location.href.indexOf("page=") == -1 ? new URL(window.location.href) : new URL(window.location.href.substring(0, window.location.href.indexOf("page="))));
			let params = new URLSearchParams(url.search);
			params.append("page", page+1);
			history.pushState({}, '', url.pathname + '?' + params.toString());

			cardGrid.innerHTML = "";

			for (let i = (pageCount * page); i < Math.min((pageCount * (page + 1)), search_results.length); i++)
			{
				cardGrid.appendChild(gridifyCard(search_results[i]));
			}

			document.getElementById("prevBtn").disabled = false;
			document.getElementById("prevBtn-footer").disabled = false;
			if (search_results.length <= (pageCount * (page + 1)))
			{
				document.getElementById("nextBtn").disabled = true;
				document.getElementById("nextBtn-footer").disabled = true;
			}

			document.body.scrollTop = 0; // For Safari
  			document.documentElement.scrollTop = 0; // For real browsers
		}

		function randomCard() {
			let i = Math.floor(Math.random() * (card_list_arrayified.length + 1));
			let card_name = card_list_arrayified[i][0];
			for (const char of specialchars)
			{
				card_name = card_name.replaceAll(char, "");
			}

			window.location = ('/cards/' + card_list_arrayified[i][11] + '/' + card_list_arrayified[i][4] + '_' + card_name);
		}
	</script>
</body>
</html>'''

	# Write the HTML content to the output HTML file
	with open(output_html_file, 'w') as file:
		file.write(html_content)

	print(f"HTML file saved as {output_html_file}")