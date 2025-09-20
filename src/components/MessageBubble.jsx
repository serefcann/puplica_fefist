import React from 'react'

const MessageBubble = ({ message }) => {
  const { type, content, timestamp } = message

  const formatTime = (date) => {
    return date.toLocaleTimeString('tr-TR', { 
      hour: '2-digit', 
      minute: '2-digit' 
    })
  }

  const getBubbleClasses = () => {
    switch (type) {
      case 'user':
        return 'user-message message-bubble'
      case 'bot':
        return 'bot-message message-bubble text-sm leading-relaxed'
      case 'error':
        return 'bg-red-100 text-red-800 message-bubble mr-auto border border-red-200'
      default:
        return 'bot-message message-bubble'
    }
  }

  const getContainerClasses = () => {
    switch (type) {
      case 'user':
        return 'flex justify-end'
      case 'bot':
      case 'error':
        return 'flex justify-start'
      default:
        return 'flex justify-start'
    }
  }

  return (
    <div className={getContainerClasses()}>
      <div className="flex flex-col max-w-xs lg:max-w-md xl:max-w-lg">
        <div className={getBubbleClasses()}>
          <div className="whitespace-pre-wrap">{content}</div>
        </div>
        <div className={`text-xs text-gray-500 mt-1 px-2 ${
          type === 'user' ? 'text-right' : 'text-left'
        }`}>
          {formatTime(timestamp)}
        </div>
      </div>
    </div>
  )
}

export default MessageBubble

