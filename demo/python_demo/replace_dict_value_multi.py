
# 替换dict里的变量为实际值，支持多个变量替换。在replacements中传入dict，key为变量，value为实际值
def replace_dict_value_multi(input_dict, replacements):
    if isinstance(input_dict, dict):
        for item in input_dict:
            if isinstance(input_dict[item], str):
                for param, value in replacements.items():
                    input_dict[item] = input_dict[item].replace(param, str(value))
            elif isinstance(input_dict[item], dict):
                replace_dict_value_multi(input_dict[item], replacements)
            elif isinstance(input_dict[item], list):
                for i in range(len(input_dict[item])):
                    if isinstance(input_dict[item][i], dict):
                        replace_dict_value_multi(input_dict[item][i], replacements)
                    elif isinstance(input_dict[item][i], str):
                        for param, value in replacements.items():
                            input_dict[item][i] = input_dict[item][i].replace(
                                param, str(value)
                            )
        return input_dict


# Example dictionary
# my_dict = {
#     'a': {
#         'b': 'Hello {param}',
#         'c': ['Hi {param}', {'d': 'Hey {param}'}]
#     }
# }

body = {
              "id": "$id$",
              "name": "temp queue",
              "locationId": "$location_id$",
              "greetingMessage": "<p>updated in Join Queue Page</p>",
              "initialServeDuration": 15,
              "serviceAgentCount": 2,
              "avgSessionServeDuration": 0,
              "summonToNoShowTime": 30,
              "noShowToRemovedTime": 120,
              "aboutToStartNotificationMinutes": 20,
              "serviceAgentInQueues": ["$agent_id$"],
            }

# Parameter-value replacements
replacements = {'$id$': '123', "$location_id$": "location123","$agent_id$":"agent123"}

result = replace_dict_value_multi(body, replacements)
print(result)
