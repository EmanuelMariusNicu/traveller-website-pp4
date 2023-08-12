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



![image](https://github.com/EmanuelMariusNicu/traveller-website-pp4/assets/108750655/932aa306-d2ad-4526-a2fd-8277d811ae34)
