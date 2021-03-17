*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***

Test Open Browser
    Open Browser    http://localhost:7272    browser=${BROWSER}
    Sleep    10s
    Title Should Be     Login Page
    [Teardown]    Close All Browsers