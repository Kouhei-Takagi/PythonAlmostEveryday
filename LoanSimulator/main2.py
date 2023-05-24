import matplotlib.pyplot as plt
import japanize_matplotlib

class LoanSimulator:
    def __init__(self, loan_amount, interest_rate, loan_term):
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term

    def calculate_loan_schedule(self):
        principal = self.loan_amount
        monthly_interest_rate = self.interest_rate / 12
        num_payments = self.loan_term * 12

        # ローンの支払いスケジュールを計算
        monthly_payment = (self.loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
        payment_schedule = []
        for _ in range(num_payments):
            interest_payment = principal * monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            principal -= principal_payment
            payment_schedule.append((principal_payment, interest_payment))

        return payment_schedule

    def plot_loan_schedule(self, payment_schedule):
        principal_payments = [payment[0] for payment in payment_schedule]
        interest_payments = [payment[1] for payment in payment_schedule]
        total_payments = [principal + interest for principal, interest in payment_schedule]

        # 支払いスケジュールを可視化
        plt.plot(principal_payments, label='元本返済額')
        plt.plot(interest_payments, label='利払い額')
        plt.plot(total_payments, label='支払い総額')
        plt.xlabel('支払い回数')
        plt.ylabel('支払い金額')
        plt.title('ローンの支払いスケジュール')
        plt.legend()
        plt.show()

# シミュレーションの実行と可視化
loan_amount = 200000
interest_rate = 0.05
loan_term = 30

loan_simulator = LoanSimulator(loan_amount, interest_rate, loan_term)
payment_schedule = loan_simulator.calculate_loan_schedule()
loan_simulator.plot_loan_schedule(payment_schedule)
