*** Settings ***
Library    Browser

*** Test Cases ***
Test Open Browser
    New Page    http://localhost:7272
    Get Title    ==     Login Page
