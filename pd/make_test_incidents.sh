#!/bin/bash
for i in {1..10}; do
curl --request POST \
  --url https://pdt-`whoami`.pagerduty.com/api/v1/incidents \
  --header 'accept: application/vnd.pagerduty+json;version=2' \
  --header "authorization: Token token=$PD_API_KEY" \
  --header 'content-type: application/json; charset=UTF-8' \
  --header "from: $(whoami)@pagerduty.com" \
  --data "{
	\"incident\": {
		\"title\": \"Test Incident $i\",
		\"service\": {
			\"id\": \"PJ85XBB\",
			\"type\": \"service_reference\"
		},
		\"escalation_policy\": {
			\"id\": \"PNY6A3N\",
			\"type\": \"escalation_policy_reference\"
		}
	}
}"
done