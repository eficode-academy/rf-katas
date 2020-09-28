*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***

Test Open Browser
    Open Browser    https://www.google.com    browser=${BROWSER}
    Sleep    10s 
    [Teardown]    Close All Browsers