
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.metrics import dp


class CurrencyApp(App):

    def build(self):

        self.title = "Currency Converter"

        # Demo exchange rates (for testing only)
        self.rates = {
            "USD": 1.0,
            "SAR": 3.75,
            "AED": 3.6725,
            "KWD": 0.307,
            "YER": None
        }

        layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(12)
        )

        title = Label(
            text="Currency Converter",
            font_size=28,
            size_hint_y=None,
            height=dp(60)
        )
        layout.add_widget(title)

        # Amount
        layout.add_widget(Label(
            text="Amount",
            font_size=18,
            size_hint_y=None,
            height=dp(35)
        ))

        self.amount = TextInput(
            text="100",
            multiline=False,
            input_filter="float",
            font_size=20,
            size_hint_y=None,
            height=dp(50),
            halign="center"
        )
        layout.add_widget(self.amount)

        # From Currency
        layout.add_widget(Label(
            text="From Currency",
            font_size=18,
            size_hint_y=None,
            height=dp(35)
        ))

        self.from_currency = Spinner(
            text="USD",
            values=("USD", "SAR", "AED", "KWD", "YER"),
            size_hint_y=None,
            height=dp(50)
        )
        layout.add_widget(self.from_currency)

        # To Currency
        layout.add_widget(Label(
            text="To Currency",
            font_size=18,
            size_hint_y=None,
            height=dp(35)
        ))

        self.to_currency = Spinner(
            text="SAR",
            values=("USD", "SAR", "AED", "KWD", "YER"),
            size_hint_y=None,
            height=dp(50)
        )
        layout.add_widget(self.to_currency)

        # Convert Button
        convert_button = Button(
            text="Convert",
            font_size=20,
            size_hint_y=None,
            height=dp(55)
        )

        convert_button.bind(on_press=self.convert)
        layout.add_widget(convert_button)

        # Result
        self.result = Label(
            text="Result will appear here",
            font_size=20
        )
        layout.add_widget(self.result)

        # Rate information
        self.rate_info = Label(
            text="Demo rates - not live market prices",
            font_size=13
        )
        layout.add_widget(self.rate_info)

        return layout

    def convert(self, instance):

        try:
            amount = float(self.amount.text)

            if amount <= 0:
                self.result.text = "Enter an amount greater than zero"
                return

            source = self.from_currency.text
            target = self.to_currency.text

            source_rate = self.rates[source]
            target_rate = self.rates[target]

            if source_rate is None or target_rate is None:
                self.result.text = (
                    "Rate not available for this currency.\n"
                    "A rate must be added first."
                )
                return

            # Currency conversion formula
            result = amount / source_rate * target_rate

            self.result.text = (
                f"{amount:,.2f} {source}\n"
                f"= {result:,.2f} {target}"
            )

            self.rate_info.text = (
                f"1 USD = {source_rate} {source}\n"
                f"1 USD = {target_rate} {target}"
            )

        except ValueError:
            self.result.text = "Please enter a valid amount"


if __name__ == "__main__":
    CurrencyApp().run()
