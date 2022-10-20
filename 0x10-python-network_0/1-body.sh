 #!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -sI "$1" | grep -i Status | cut -d " " -f2
