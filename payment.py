from abc import ABC,abstractmethod
class Payment(ABC):

    def __init__(self,amount,transaction_id,payment_status):
        self.__amount = amount
        self.__transaction_id = transaction_id
        self.__payment_status = payment_status
        self.__created_at = datetime.now()

    @abstractmethod
    def process_payment(self):







