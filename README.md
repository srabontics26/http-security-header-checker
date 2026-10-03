# HTTP Security Header Checker

A simple Python tool that checks a website for common HTTP security headers.

## About the Project

I made this project to practice Python networking and understand how HTTP security headers can help improve website security.

The program sends a normal HTTP request and checks whether several commonly used security headers are present in the response.

## Features

- Checks common HTTP security headers
- Shows the HTTP response status
- Reports present and missing headers
- Accepts a website URL from the user
- Uses Python's built-in urllib module

## Security Headers Checked

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy

## Technologies Used

- Python 3
- urllib

## How to Run

```bash
python security_headers.py
