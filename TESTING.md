# TravellersWorld Testing
The testing.md file provides an overview of the testing conducted on the TravellersWorld website. It covers code validation, accessibility, performance, testing on various devices, browser compatibility, testing user stories, and user feedback and improvements. Each section describes the tools used, the issues found (if any), and the corresponding test results.

## Table of Content

1. [Code Validation](#html-validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Python Validation](#python-validation)
2. [Accessibility](#accessibility)
3. [Performance](#performance)
    1. [Desktop Performance](#desktop-performance)
    2. [Mobile Performance](#mobile-performance)
4. [Performing tests on various devices](#performing-tests-on-various-devices)
5. [Browser compability](#browser-compability)
6. [Manual Testing](#manual-testing)
    1. [Testing user stories](#testing-user-stories)
    2. [User Experience and Improvements](#user-experience-and-improvements)
    3. [Full testing](#full-testing)
8. [Summary](#summary)


## Code Validation

### HTML Validation
[W3C Markup Validation](https://validator.w3.org/) is a service provided by the W3C that allows you to validate your HTML code against the official specifications. It checks for syntax errors, improper tag usage, and other issues that may affect the structure and semantics of your web pages. Validating your HTML code with W3C Markup Validation helps ensure that your pages are well-formed and adhere to web standards

All pages passed through the validation and the code was pasted in and I used a filter to remove issues related to the Django templating system. <details><summary>See filter</summary>![Result](/docs/validation/html/filter.png)</details>

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|base| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/base.png)</details>| :white_check_mark:
|index| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/index.png)</details>| :white_check_mark:
|add_trip| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/add_trip.png)</details>| :white_check_mark:
|edit_trip| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/edit_trip.png)</details>| :white_check_mark:
|browse| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/browse.png)</details>| :white_check_mark:
|post_detail| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/post_detail.png)</details>| :white_check_mark:
|search_card| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/search_card)</details>| :white_check_mark:
|search_results| No errors | <details><summary>Screenshot of result</summary>![Result](/docs/validation/html/search_results.png)</details>| :white_check_mark:

### CSS Validation
[W3C Jigsaw](https://jigsaw.w3.org/css-validator/) is a tool provided by the World Wide Web Consortium (W3C) that allows you to validate and check the correctness of your HTML and CSS code. It helps ensure that your web pages comply with the standards set by the W3C, promoting interoperability and accessibility.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
|CSS file | No errors |[Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/932aa306-d2ad-4526-a2fd-8277d811ae34)| :white_check_mark:

### Python Validation 
[PEP 8](https://pep8ci.herokuapp.com/) is a style guide for writing Python code to ensure consistency and readability. It provides guidelines on how to format code, naming conventions for variables and functions, and other best practices. Following PEP 8 helps to improve code quality, readability, and maintainability.

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:



[Back to the top](#table-of-content)

<br>

## Accessibility
[The WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) was used to assess the accessibility of the website. WAVE helps identify potential accessibility issues and provides guidance on how to improve the accessibility of web content.
During the evaluation, no issues were identified.
![image](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/93094827-8170-428c-9bac-4e2322d9c114)

[Back to the top](#table-of-content)


<br>

## Performance 
The Traveller World website was tested using [Google Lighthouse in Google Chrome Developer Tools](https://developer.chrome.com/docs/lighthouse/). The performance scores were evaluated for both desktop and mobile devices. Here are the summarized results:

### Desktop Performance
- The majority of pages received scores above 90/100, indicating excellent performance.


| **Tested** | **Performance Score** | **View Result** | **Pass** |
--- | --- | --- | :---:
|index| 96 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/cc7ecee7-4928-4ba7-85d1-f928733461f6)</details> | :white_check_mark:
|browse| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/17d1f5b9-1f02-4df8-9c7c-1fa344b0a5dc)</details> | :white_check_mark:
|signup| 99 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/35b6d493-1852-41db-8544-66515498a802)</details> | :white_check_mark:
|login | 99 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/421f9f64-b775-4f02-b8d1-9d43f10fe016)</details> | :white_check_mark:
|post_detail| 85 / 100 |<details><summary>Screenshotofresult</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/e16508ff-2e75-42c7-957d-f62431abd1ff)</details>|:white_check_mark:
|search_results| 85 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/b0400772-a5bc-45dc-bf08-c6e46b3de2fa)</details>|:white_check_mark:

### Mobile Performance
- The majority of pages received scores above 90/100, indicating excellent performance.

  
| **Tested** | **Performance Score** | **View Result** | **Pass** |
--- | --- | --- | :---:
|index| 96 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/5f5d63ff-0d8d-4497-b0d2-ab8906ea1520)
</details> | :white_check_mark:
|browse| 67 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/13bb7ef5-61b0-4bf5-bcec-cb363e73af14)
</details> | :white_check_mark:
|signup| 94 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/a400b12b-79bc-4620-b744-4cf9c7b0af4d)
</details> | :white_check_mark:
|login | 94 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/5bc919a5-56b0-4ac5-a20c-c7cb3643cfa3)
</details> | :white_check_mark:
|post_detail| 85 / 100 |<details><summary>Screenshotofresult</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/4b8793c8-8117-4253-a632-26e8c8e1ee6e)
</details>|:white_check_mark:
|search_results| 85 / 100 | <details><summary>Screenshot of result</summary>![Result](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/dfcf0e6d-6f09-4174-9d60-91f714c3a9c1)
</details>|:white_check_mark:
