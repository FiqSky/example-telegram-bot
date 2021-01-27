from datetime import datetime


def sample_responses(input_text):
    uses_message = str(input_text).lower()

    if uses_message in ("hello", "hi", "cuy"):
        return "Hi, whats app bro?"

    if uses_message in ("who are you", "who are you?"):
        return "Im amazing bro! And about you?"

    if uses_message in ("fiqih", "fiqsky", "piq", "fiq"):
        return "My name is Fiqih! \n" \
               "Les's connect https://www.linkedin.com/in/fiqihfirdausmaulana \n" \
               "Persoal web: https://fiqq.xyz \n" \
               "Github: https://github.com/FiqSky \n" \
               "Fell free to be message me"

    if uses_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I dont understand bro! try calling my name"
